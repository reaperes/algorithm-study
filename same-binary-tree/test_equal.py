import unittest
from equal import Node, equal


class TestEqual(unittest.TestCase):
    def test_equal(self):
        src = Node(0)

        src_left = Node(1)
        src.left = src_left

        tar = Node(0)
        tar_left = Node(1)
        tar.left = tar_left

        self.assertTrue(equal(src, tar))

if __name__ == '__main__':
    unittest.main()