import unittest

from complement import complement


class TestComplement(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, complement(5))

    def test2(self):
        self.assertEqual(0, complement(1))
