# Let n be the number of nodes in the tree
#
# Time: O(n)
# Space: O(n)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # Invert left and right
        root.left, root.right = root.right, root.left

        # Invert sub-tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
