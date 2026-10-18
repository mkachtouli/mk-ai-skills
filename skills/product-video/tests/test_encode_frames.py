import importlib.util
import os
from pathlib import Path
import shutil
import struct
import tempfile
import unittest
import zlib

path=Path(__file__).resolve().parents[1]/'scripts/encode_frames.py'
spec=importlib.util.spec_from_file_location('encode_frames',path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


def png(path,width=64,height=64,colour=(170,140,80)):
    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)
    pixels=b''.join(b'\0'+bytes(colour)*width for _ in range(height))
    path.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',width,height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(pixels))+chunk(b'IEND',b''))


class EncoderTests(unittest.TestCase):
    def test_reject_gaps_dimensions_and_duration_before_encoding(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);png(root/'0000.png');png(root/'0002.png')
            with self.assertRaises(ValueError):module.sequence(root)
            (root/'0002.png').rename(root/'0001.png');png(root/'0001.png',width=62)
            with self.assertRaises(ValueError):module.sequence(root)
            png(root/'0001.png')
            with self.assertRaises(ValueError):module.encode(root,root/'out.mp4',fps=1,max_seconds=1)
            with self.assertRaises(ValueError):module.encode(root,root/'out.mp4',fps=float('nan'))

    def test_actual_ffmpeg_roundtrip(self):
        ffmpeg=os.environ.get('FFMPEG_BINARY') or shutil.which('ffmpeg')
        if not ffmpeg:self.skipTest('Set FFMPEG_BINARY for the actual encode/decode test')
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);frames=root/'frames';frames.mkdir()
            for i,c in enumerate([(180,145,80),(160,135,95),(190,160,110)]):png(frames/f'{i:04d}.png',colour=c)
            output=root/'movie.mp4';report=module.encode(frames,output,fps=8,max_seconds=1,ffmpeg=ffmpeg)
            self.assertEqual(report['decodedFrames'],3);self.assertEqual(report['resolution'],[64,64]);self.assertFalse(report['audio'])
            self.assertAlmostEqual(report['durationSeconds'],.375,delta=.02)
            with self.assertRaises(ValueError):module.encode(frames,output,ffmpeg=ffmpeg)


if __name__=='__main__':unittest.main()
