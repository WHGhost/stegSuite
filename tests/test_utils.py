from unittest import TestCase
from stegsuite.utils import *

class Func_steg_alterbits_TestCase(TestCase):

    def test_int(self):
        test_string = "1234567890AZERTYUIOPQSDFGHJKLMWX"
        test_bytes = b'Super Secret Message of the Doom'
        b = bytearray(test_string.encode('utf-8'))
        steg_encode_alterbits(b, test_bytes, 255),
        self.assertEqual(b, test_bytes)

    def test_iter(self):
        test_string = "1234567890AZERTYUIOPQSDFGHJKLMWX"
        test_bytes = b'Super Secret Message of the Doom'
        b = bytearray(test_string.encode('utf-8'))
        steg_encode_alterbits(b, test_bytes, [255, ] * len(b)),
        self.assertEqual(b, test_bytes)

    def test_func(self):
        test_string = "1234567890AZERTYUIOPQSDFGHJKLMWX"
        test_bytes = b'Super Secret Message of the Doom'
        b = bytearray(test_string.encode('utf-8'))
        steg_encode_alterbits(b, test_bytes, lambda a, b: 255),
        self.assertEqual(b, test_bytes)

    def test_nullmask(self):
        test_string = "1234567890AZERTYUIOPQSDFGHJKLMW"
        test_bytes = b'Super Secret Message of the Doom'
        b = bytearray(test_string.encode('utf-8'))
        with self.assertRaises(CoverError):
            steg_encode_alterbits(b, test_bytes, 0)

    def test_covertype(self):
        with self.assertRaises(TypeError):
            steg_encode_alterbits(b'test', b'Lolmdr', 1)

    def test_streamtype(self):
        with self.assertRaises(TypeError):
            steg_encode_alterbits(bytearray(b'test'), "", 1)

    def test_masktype(self):
        with self.assertRaises(TypeError):
            steg_encode_alterbits(bytearray(b'test'), b"A cool place to hide things", "3")
