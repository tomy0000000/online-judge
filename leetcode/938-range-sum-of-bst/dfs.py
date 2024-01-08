# Let n be the number of nodes in the tree.
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        at_least_low = bool(low <= root.val)
        at_most_high = bool(root.val <= high)

        left = self.rangeSumBST(root.left, low, high) if at_least_low else 0
        right = self.rangeSumBST(root.right, low, high) if at_most_high else 0
        val = root.val if at_least_low and at_most_high else 0

        return val + left + right
