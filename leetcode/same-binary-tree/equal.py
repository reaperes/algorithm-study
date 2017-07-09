"""
quiz: https://leetcode.com/problems/same-tree/#/description

Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# WHen 'n' is number of nodes
# O(n), Ω(n), Θ(n)
def equal(source, target):
    if (source is None) and (target is None):
        return True

    if (source is None) or (target is None):
        return False

    if source.val != target.val:
        return False

    return equal(source.left, target.left) and equal(source.right, target.right)