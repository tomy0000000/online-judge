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
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)

        if not left and not right and root.val == target:
            return None

        return TreeNode(root.val, left, right)
