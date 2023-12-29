# Let n be the length of the tree
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
    maxi: int

    def path_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.path_sum(root.left)
        right = self.path_sum(root.right)

        self.maxi = max(
            self.maxi,
            root.val,
            root.val + left + right,
            root.val + left,
            root.val + right,
        )

        return root.val + max(left, right, 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = root.val
        self.path_sum(root)
        return self.maxi
