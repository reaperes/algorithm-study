import unittest

from heightbalancedtree import TreeNode, is_balanced


class TestHeightBalancedTree(unittest.TestCase):
    def test(self):
        left = TreeNode(2)
        root = TreeNode(1)
        root.left = left

        self.assertEqual(True, is_balanced(root))
