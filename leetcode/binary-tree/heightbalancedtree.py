"""https://leetcode.com/problems/balanced-binary-tree/#/description
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_depth(node):
    if node is None:
        return 0

    return 1 + max(get_depth(node.left), get_depth(node.right))


def is_balanced(root):
    if root is None:
        return True

    left = get_depth(root.left)
    right = get_depth(root.right)

    return abs(left - right) < 2 and is_balanced(root.left) and is_balanced(root.right)
