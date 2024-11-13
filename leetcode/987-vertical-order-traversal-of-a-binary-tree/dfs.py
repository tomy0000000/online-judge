# Let n be the number of nodes in the input tree
#
# Time: O(n * log(n))
# Space: O(n)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        stack = [(root, 0, 0)]
        tuples = []
        while stack:
            node, col, row = stack.pop()
            tuples.append((col, row, node.val))
            if node.left:
                stack.append((node.left, col - 1, row + 1))
            if node.right:
                stack.append((node.right, col + 1, row + 1))

        tuples.sort()
        by_cols = [[]]
        this_col = tuples[0][0]
        for col, row, val in tuples:
            if col != this_col:
                by_cols.append([])
                this_col = col
            by_cols[-1].append(val)

        return by_cols
