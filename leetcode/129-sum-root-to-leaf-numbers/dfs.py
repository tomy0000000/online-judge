# Let n be the number of nodes in the tree
#
# Time: O(n)
# Space: O(1)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def numbers(self, root: Optional[TreeNode]) -> list[str]:
        if not root:
            return [""]

        if not root.left and not root.right:
            return [root.val]

        results = []
        if root.left:
            results += [f"{root.val}{n}" for n in self.numbers(root.left)]
        if root.right:
            results += [f"{root.val}{n}" for n in self.numbers(root.right)]
        return results

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(int(n) for n in self.numbers(root))
