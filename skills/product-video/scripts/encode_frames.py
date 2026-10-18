#!/usr/bin/env python3
"""Encode consecutive numbered PNG frames and verify the resulting silent MP4."""
import argparse
import json
import math
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile


def sequence(folder):
    files = list(Path(folder).glob('*.png'))
    if not files or any(not re.fullmatch(r'\d+\.png', f.name) for f in files):
        raise ValueError('Frames folder must contain numbered PNGs, e.g. 0000.png')
    files.sort(key=lambda f: int(f.stem)); padding = len(files[0].stem)
    indices = [int(f.stem) for f in files]
    if any(len(f.stem) != padding for f in files) or indices != list(range(indices[0], indices[0]+len(files))):
        raise ValueError('Frame numbers must have consistent padding and no gaps/duplicates')
    dimensions = set()
    for frame in files:
        with frame.open('rb') as stream:
            header = stream.read(24)
        if len(header) != 24 or header[:8] != b'\x89PNG\r\n\x1a\n' or header[12:16] != b'IHDR':
            raise ValueError(f'Invalid PNG header: {frame.name}')
        dimensions.add(struct.unpack_from('>II', header, 16))
    if len(dimensions) != 1:
        raise ValueError('All frames must have identical dimensions')
    size = dimensions.pop()
    if not all(n > 0 and n % 2 == 0 for n in size):
        raise ValueError('H.264 yuv420p requires positive even dimensions')
    return files, padding, size


def encode(folder, output, fps=24, max_seconds=15, ffmpeg='ffmpeg', overwrite=False):
    if not math.isfinite(fps) or not math.isfinite(max_seconds) or fps <= 0 or max_seconds <= 0:
        raise ValueError('FPS and maximum duration must be positive finite numbers')
    files, padding, size = sequence(folder); duration = len(files)/fps
    if duration > max_seconds+1e-8:
        raise ValueError(f'{duration:.3f}s exceeds requested cap {max_seconds}s')
    output = Path(output)
    if output.suffix.lower() != '.mp4':
        raise ValueError('Output must use .mp4')
    if output.exists() and not overwrite:
        raise ValueError('Output exists; use a new revision or --overwrite')
    executable = shutil.which(str(ffmpeg))
    if not executable:
        raise ValueError('FFmpeg unavailable; pass --ffmpeg /path/to/ffmpeg')
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix='.mp4', dir=output.parent, delete=False) as stream:
        temporary = Path(stream.name)
    try:
        command = [executable, '-hide_banner', '-loglevel', 'error', '-y', '-framerate', str(fps),
                   '-start_number', files[0].stem, '-i', str(Path(folder)/f'%0{padding}d.png'),
                   '-frames:v', str(len(files)), '-an', '-vf',
                   'scale=in_range=full:out_range=tv:out_color_matrix=bt709', '-color_range', 'tv',
                   '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
                   '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
                   '-movflags', '+faststart', str(temporary)]
        subprocess.run(command, check=True, capture_output=True, text=True)
        decoded = subprocess.run([executable, '-hide_banner', '-i', str(temporary), '-map', '0:v:0',
                                  '-progress', 'pipe:1', '-nostats', '-f', 'null', '-'],
                                 check=True, capture_output=True, text=True)
        frames = [int(n) for n in re.findall(r'^frame=(\d+)$', decoded.stdout, re.M)]
        match = re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)', decoded.stderr)
        video_lines = [line for line in decoded.stderr.splitlines() if 'Video:' in line]
        if not frames or frames[-1] != len(files) or not match or not video_lines:
            raise ValueError('Encoded output frame count/metadata could not be verified')
        h, m, s = map(float, match.groups()); actual_duration = h*3600+m*60+s
        actual_size = re.search(r'\b(\d{2,5})x(\d{2,5})\b', video_lines[0])
        if (abs(actual_duration-duration) > .06 or actual_duration > max_seconds+.01
                or not actual_size or tuple(map(int, actual_size.groups())) != size
                or 'h264' not in video_lines[0] or 'yuv420p' not in video_lines[0]
                or 'Audio:' in decoded.stderr):
            raise ValueError('Encoded output does not match the requested video specification')
        temporary.replace(output)
        return {'output': str(output), 'durationSeconds': actual_duration, 'decodedFrames': frames[-1],
                'resolution': list(size), 'fpsRequested': fps, 'audio': False, 'codec': 'h264',
                'pixelFormat': 'yuv420p', 'fileBytes': output.stat().st_size}
    except subprocess.CalledProcessError as error:
        raise ValueError('FFmpeg failed: '+error.stderr[-2000:]) from error
    finally:
        temporary.unlink(missing_ok=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--frames', required=True); p.add_argument('--output', required=True)
    p.add_argument('--fps', type=float, default=24); p.add_argument('--max-seconds', type=float, default=15)
    p.add_argument('--ffmpeg', default='ffmpeg'); p.add_argument('--overwrite', action='store_true')
    p.add_argument('--report', help='Optional JSON output-check report')
    a = p.parse_args()
    try:
        report = encode(a.frames, a.output, a.fps, a.max_seconds, a.ffmpeg, a.overwrite)
    except (OSError, ValueError) as error:
        p.exit(2, f'Encoding failed: {error}\n')
    text = json.dumps(report, indent=2)
    if a.report:
        Path(a.report).write_text(text+'\n')
    print(text)


if __name__ == '__main__':
    main()
