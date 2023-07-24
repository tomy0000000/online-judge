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
        mini: Optional[int] = None,
        maxi: Optional[int] = None,
    ):
        if not root:
            return True

        print(f"{root.val=} {mini=} {maxi=}")
        if mini and root.val <= mini:
            print(f"ERROR: {root.val} too small {mini}")
            return False
        if maxi and maxi <= root.val:
            print(f"ERROR: {root.val} too big {maxi}")
            return False

        if root.left:
            if root.val <= root.left.val:
                return False
            if not self.valid_bst_with_min_max(
                root.left, mini=mini, maxi=min(maxi, root.val) if maxi else root.val
            ):
                return False

        if root.right:
            if root.right.val <= root.val:
                return False
            if not self.valid_bst_with_min_max(
                root.right, mini=max(mini, root.val) if mini else root.val, maxi=maxi
            ):
                return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid_bst_with_min_max(root)
