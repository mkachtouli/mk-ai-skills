#!/usr/bin/env python3
"""Inspect ordinary static GLB vertex bounds. Not a full glTF validator."""
import argparse
import json
import math
from pathlib import Path
import struct


def multiply(a, b):
    return [[sum(a[r][k] * b[k][c] for k in range(4)) for c in range(4)] for r in range(4)]


def transform(node):
    if 'matrix' in node:
        if any(k in node for k in ('translation', 'rotation', 'scale')):
            raise ValueError('Node mixes matrix and TRS')
        m = node['matrix']
        if len(m) != 16:
            raise ValueError('Expected a 4x4 node matrix')
        return [[m[c * 4 + r] for c in range(4)] for r in range(4)]
    x, y, z, w = node.get('rotation', [0, 0, 0, 1])
    sx, sy, sz = node.get('scale', [1, 1, 1])
    tx, ty, tz = node.get('translation', [0, 0, 0])
    return [
        [(1-2*y*y-2*z*z)*sx, (2*x*y-2*z*w)*sy, (2*x*z+2*y*w)*sz, tx],
        [(2*x*y+2*z*w)*sx, (1-2*x*x-2*z*z)*sy, (2*y*z-2*x*w)*sz, ty],
        [(2*x*z-2*y*w)*sx, (2*y*z+2*x*w)*sy, (1-2*x*x-2*y*y)*sz, tz],
        [0, 0, 0, 1],
    ]


def inspect(path):
    raw = Path(path).read_bytes()
    if len(raw) < 20:
        raise ValueError('Truncated GLB')
    magic, version, length = struct.unpack_from('<4sII', raw)
    if magic != b'glTF' or version != 2 or length != len(raw):
        raise ValueError('Invalid GLB 2.0 header or length')
    chunks = []; offset = 12
    while offset < len(raw):
        if offset + 8 > len(raw):
            raise ValueError('Truncated chunk header')
        size, kind = struct.unpack_from('<II', raw, offset); offset += 8
        if size % 4 or offset + size > len(raw):
            raise ValueError('Invalid chunk length/alignment')
        chunks.append((kind, raw[offset:offset+size])); offset += size
    if not chunks or chunks[0][0] != 0x4E4F534A:
        raise ValueError('Missing first JSON chunk')
    doc = json.loads(chunks[0][1]); bins = [data for kind, data in chunks if kind == 0x004E4942]
    if len(bins) != 1 or len(doc.get('buffers', [])) != 1 or doc['buffers'][0].get('uri'):
        raise ValueError('Expected one embedded GLB buffer; external buffers unsupported')
    binary = bins[0]
    if doc['buffers'][0]['byteLength'] > len(binary):
        raise ValueError('Buffer length exceeds binary chunk')
    if doc.get('animations') or doc.get('skins'):
        raise ValueError('Animations and skins are unsupported; use a glTF runtime')
    if any(e in doc.get('extensionsRequired', []) for e in ('KHR_draco_mesh_compression', 'EXT_meshopt_compression')):
        raise ValueError('Compressed geometry unsupported')

    def accessor(index, positions=False):
        a = doc['accessors'][index]
        if 'sparse' in a or 'bufferView' not in a or a.get('normalized'):
            raise ValueError('Sparse, missing-view or normalized accessor unsupported')
        v = doc['bufferViews'][a['bufferView']]
        if v.get('buffer', 0) != 0 or v.get('extensions', {}).get('EXT_meshopt_compression'):
            raise ValueError('External/compressed view unsupported')
        if positions:
            if a['componentType'] != 5126 or a['type'] != 'VEC3':
                raise ValueError('Expected float VEC3 positions')
            fmt, width = '<fff', 12
        else:
            if a['type'] != 'SCALAR' or a['componentType'] not in (5121, 5123, 5125):
                raise ValueError('Invalid index accessor')
            fmt, width = {5121: ('<B', 1), 5123: ('<H', 2), 5125: ('<I', 4)}[a['componentType']]
        stride = v.get('byteStride', width); relative = a.get('byteOffset', 0)
        if relative < 0 or stride < width or a['count'] < 0:
            raise ValueError('Invalid accessor layout')
        end = relative + max(0, a['count']-1)*stride + (width if a['count'] else 0)
        start = v.get('byteOffset', 0)
        if end > v['byteLength'] or start < 0 or start+v['byteLength'] > len(binary):
            raise ValueError('Accessor exceeds buffer view')
        values = [struct.unpack_from(fmt, binary, start+relative+i*stride) for i in range(a['count'])]
        return values if positions else [value[0] for value in values]

    result = []; all_points = []
    def bounds(points):
        lo = [min(p[i] for p in points) for i in range(3)]; hi = [max(p[i] for p in points) for i in range(3)]
        return {'min': lo, 'max': hi, 'size': [hi[i]-lo[i] for i in range(3)]}

    def walk(index, parent, trail):
        if index in trail:
            raise ValueError('Cycle in node hierarchy')
        node = doc['nodes'][index]
        if 'skin' in node or node.get('weights'):
            raise ValueError('Skin/morph weights unsupported')
        matrix = multiply(parent, transform(node)); points = []
        if 'mesh' in node:
            for primitive in doc['meshes'][node['mesh']]['primitives']:
                if primitive.get('targets') or primitive.get('extensions', {}).get('KHR_draco_mesh_compression'):
                    raise ValueError('Morph/compressed geometry unsupported')
                source = accessor(primitive['attributes']['POSITION'], positions=True)
                indices = accessor(primitive['indices']) if 'indices' in primitive else range(len(source))
                for i in indices:
                    if not 0 <= i < len(source):
                        raise ValueError('Index exceeds position accessor')
                    v = [*source[i], 1]; p = [sum(matrix[r][k]*v[k] for k in range(4)) for r in range(3)]
                    if not all(math.isfinite(n) for n in p):
                        raise ValueError('Non-finite vertex')
                    points.append(p)
        if points:
            result.append({'nodeIndex': index, 'name': node.get('name', ''), 'boundsMetres': bounds(points)})
            all_points.extend(points)
        for child in node.get('children', []):
            walk(child, matrix, trail | {index})

    identity = [[int(r == c) for c in range(4)] for r in range(4)]
    for node in doc['scenes'][doc.get('scene', 0)].get('nodes', []):
        walk(node, identity, set())
    if not all_points:
        raise ValueError('Default scene has no inspected geometry')
    return {'units': 'metres (glTF convention; confirm author scale)', 'boundsMetres': bounds(all_points),
            'nodes': result, 'scope': 'Static default-scene referenced vertices, not complete glTF validation'}


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('model'); p.add_argument('--output')
    args = p.parse_args()
    try:
        report = inspect(args.model)
    except (ValueError, KeyError, IndexError, TypeError, OSError, struct.error) as error:
        p.exit(2, f'Inspection failed: {error}\n')
    text = json.dumps(report, indent=2, allow_nan=False)
    if args.output:
        Path(args.output).write_text(text+'\n')
    else:
        print(text)


if __name__ == '__main__':
    main()
