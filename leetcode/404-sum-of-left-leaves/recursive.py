# Let n be the number of nodes in the input tree
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode], is_left: bool = False) -> int:
        if not root.left and not root.right:
            return root.val if is_left else 0

        left_val = self.sumOfLeftLeaves(root.left, True) if root.left else 0
        right_val = self.sumOfLeftLeaves(root.right, False) if root.right else 0
        return left_val + right_val
