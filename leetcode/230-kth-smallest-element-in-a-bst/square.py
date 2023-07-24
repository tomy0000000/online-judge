# Let n be the number of nodes in the tree.
#
# Time: O(n ^ 2)
# Space: O(1)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def nodes_count(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.nodes_count(root.left) + self.nodes_count(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left_depth = self.nodes_count(root.left)
        if left_depth == k - 1:
            return root.val
        elif left_depth < k - 1:
            return self.kthSmallest(root.right, k - left_depth - 1)
        else:
            return self.kthSmallest(root.left, k)
