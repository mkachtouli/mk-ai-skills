import importlib.util
import json
import math
from pathlib import Path
import struct
import tempfile
import unittest

path = Path(__file__).resolve().parents[1]/'scripts/inspect_glb.py'
spec = importlib.util.spec_from_file_location('inspect_glb', path)
module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)


def fixture(path, mutate=None):
    vertices = b''.join(struct.pack('<ffff', *v, 123) for v in [(0,0,0), (1,0,0), (0,1,0), (99,99,99)])
    binary = vertices+struct.pack('<HHH', 0,1,2)
    doc = {'asset': {'version':'2.0'}, 'buffers':[{'byteLength':len(binary)}],
           'bufferViews':[{'buffer':0,'byteOffset':0,'byteLength':64,'byteStride':16},
                          {'buffer':0,'byteOffset':64,'byteLength':6}],
           'accessors':[{'bufferView':0,'componentType':5126,'count':4,'type':'VEC3'},
                        {'bufferView':1,'componentType':5123,'count':3,'type':'SCALAR'}],
           'meshes':[{'primitives':[{'attributes':{'POSITION':0},'indices':1}]}],
           'nodes':[{'translation':[1,2,3],'rotation':[0,0,math.sqrt(.5),math.sqrt(.5)],
                     'scale':[2,3,4],'children':[1]},
                    {'name':'test component','mesh':0,'matrix':[1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1]}],
           'scenes':[{'nodes':[0]}], 'scene':0}
    if mutate: mutate(doc)
    data=json.dumps(doc).encode();data+=b' '*((-len(data))%4);binary+=b'\0'*((-len(binary))%4)
    chunks=struct.pack('<II',len(data),0x4E4F534A)+data+struct.pack('<II',len(binary),0x004E4942)+binary
    path.write_bytes(struct.pack('<4sII',b'glTF',2,len(chunks)+12)+chunks)


class InspectorTests(unittest.TestCase):
    def test_interleaved_indexed_geometry_and_nested_transforms(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'model.glb';fixture(p);report=module.inspect(p)
            for actual,expected in zip(report['boundsMetres']['min'],[-2,4,3]):self.assertAlmostEqual(actual,expected)
            for actual,expected in zip(report['boundsMetres']['max'],[1,6,3]):self.assertAlmostEqual(actual,expected)
            self.assertEqual(report['nodes'][0]['name'],'test component')

    def test_unhandled_geometry_and_truncation_are_rejected(self):
        changes=[lambda d:d.update(animations=[{}]),
                 lambda d:d['accessors'][0].update(sparse={}),
                 lambda d:d.update(extensionsRequired=['KHR_draco_mesh_compression']),
                 lambda d:d['nodes'][1].update(children=[0]),
                 lambda d:d['bufferViews'][0].update(byteLength=8)]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'model.glb'
            for change in changes:
                fixture(p,change)
                with self.assertRaises(ValueError):module.inspect(p)
            fixture(p);p.write_bytes(p.read_bytes()[:-1])
            with self.assertRaises(ValueError):module.inspect(p)


if __name__=='__main__':unittest.main()
