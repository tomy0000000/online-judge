# Let n be the number of nodes in the binary tree.
#
# Time: O(n)
# Space: O(1)

from collections import Counter
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(
        self, root: Optional[TreeNode], path: Optional[Counter] = None
    ) -> int:
        path = Counter() if not path else path

        if not root.left and not root.right:
            path[root.val] += 1
            ans = int(len([n for n in path.values() if n % 2 != 0]) <= 1)
            path[root.val] -= 1
            return ans

        path[root.val] += 1
        left = self.pseudoPalindromicPaths(root.left, path) if root.left else 0
        right = self.pseudoPalindromicPaths(root.right, path) if root.right else 0
        path[root.val] -= 1

        return left + right
