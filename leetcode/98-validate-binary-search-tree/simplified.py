# Let n be the number of nodes in the tree.
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
    def valid_bst_with_min_max(
        self,
        root: Optional[TreeNode],
        mini: Optional[int] = float("-inf"),
        maxi: Optional[int] = float("inf"),
    ):
        if not root:
            return True

        if not mini < root.val < maxi:
            return False

        return self.valid_bst_with_min_max(
            root.left, mini=mini, maxi=root.val
        ) and self.valid_bst_with_min_max(root.right, mini=root.val, maxi=maxi)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid_bst_with_min_max(root)
