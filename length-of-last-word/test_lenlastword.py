import unittest
from lenlastword import get_len


class TestGetLen(unittest.TestCase):
    def test(self):
        self.assertEqual(5, get_len("Hello World"))

    def test2(self):
        self.assertEqual(1, get_len("a "))


if __name__ == '__main__':
    unittest.main()
