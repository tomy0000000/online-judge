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
    diameter: int

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.depth(root.left)
        right = self.depth(root.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
