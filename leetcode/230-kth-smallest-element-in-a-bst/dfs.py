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
    def __init__(self):
        self.tree_list = []

    def DFS(self, root: Optional[TreeNode]):
        if root.left:
            self.DFS(root.left)
        self.tree_list.append(root.val)
        if root.right:
            self.DFS(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.DFS(root)
        return self.tree_list[k - 1]
