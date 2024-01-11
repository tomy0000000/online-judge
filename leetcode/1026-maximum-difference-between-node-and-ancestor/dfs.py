# Let n be the number of nodes in the tree.
#
# Time: O(n)
# Space: O(1)

from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: Optional[TreeNode]) -> tuple[int, int, int]:  # ans, min, max
        if not root:
            return 0, inf, -inf

        val = root.val
        if not root.left and not root.right:
            return 0, val, val

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        mini = min(left[1], right[1])
        maxi = max(left[2], right[2])
        ans = max(abs(val - mini), abs(val - maxi), left[0], right[0])
        return ans, min(mini, val), max(maxi, val)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]
