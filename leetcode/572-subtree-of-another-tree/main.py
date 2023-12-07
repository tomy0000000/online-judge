# Let n be the length of the tree
#
# Time: O(n)
# Space: O(1)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def wrapped(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode], matched: bool
    ) -> bool:
        if root is None and subRoot is None:
            return True

        if (root is None and subRoot) or (root and subRoot is None):
            return False

        if root.val == subRoot.val:
            if self.wrapped(root.left, subRoot.left, True) and self.wrapped(
                root.right, subRoot.right, True
            ):
                return True

        if not matched:
            if root.left and self.wrapped(root.left, subRoot, False):
                return True
            if root.right and self.wrapped(root.right, subRoot, False):
                return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.wrapped(root, subRoot, False)
