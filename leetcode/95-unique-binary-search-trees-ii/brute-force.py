# Time: O((n!) * n log n)
# Space: O(1)


import itertools
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __hash__(self: "TreeNode"):
        return 0  # Set require this

    def __eq__(self: "TreeNode", other: "TreeNode"):
        if self and not other:
            return False
        if not self and other:
            return False
        if self.val != other.val:
            return False
        if self.left != other.left:
            return False
        if self.right != other.right:
            return False
        return True

    def insert(self: "TreeNode", n: int):
        if n > self.val:
            if not self.right:
                self.right = TreeNode(n)
            else:
                self.right.insert(n)
        else:
            if not self.left:
                self.left = TreeNode(n)
            else:
                self.left.insert(n)


class Solution:
    def genTree(self, perm):
        root = TreeNode(perm[0])
        for n in perm[1:]:
            root.insert(n)
        return root

    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        trees = set()
        for perm in itertools.permutations(range(1, n + 1), n):
            trees.add(self.genTree(perm))
        return trees
