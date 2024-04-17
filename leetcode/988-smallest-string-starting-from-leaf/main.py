# Let n be the number of nodes in the tree
#
# Time: O(n)
# Space: O(n log n)

import string
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def all_combs(self, root: Optional[TreeNode]) -> str:
        if not root:
            return []

        if not root.left and not root.right:
            return [[root.val]]

        return [
            l + [root.val]
            for l in self.all_combs(root.left) + self.all_combs(root.right)
        ]

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        int_list = self.all_combs(root)
        return "".join([string.ascii_lowercase[i] for i in min(int_list)])
