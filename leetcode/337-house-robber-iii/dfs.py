# Let n be the number of nodes in the tree.
#
# Time: O(n)
# Space: O(1)


from functools import cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def rob(self, root: Optional[TreeNode], allowed: Optional[bool] = True) -> int:
        if not root:
            return 0

        ans = []
        if allowed:
            left = self.rob(root.left, False)
            right = self.rob(root.right, False)
            ans.append(root.val + left + right)

        left = self.rob(root.left, True)
        right = self.rob(root.right, True)
        ans.append(left + right)

        return max(ans)
