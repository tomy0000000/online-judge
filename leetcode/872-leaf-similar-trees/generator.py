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
    def leaf(self, root: Optional[TreeNode]) -> int:
        if root:
            if not root.left and not root.right:
                yield root.val

            yield from self.leaf(root.left)
            yield from self.leaf(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_1 = self.leaf(root1)
        leaves_2 = self.leaf(root2)
        while (n1 := next(leaves_1, False)) | (n2 := next(leaves_2, False)):
            # Use | instead of or to avoid short-circuiting
            if n1 != n2:
                return False
        return True
