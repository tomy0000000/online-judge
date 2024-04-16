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
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        row = [root]
        for _ in range(depth - 2):
            new_row = []
            for node in row:
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)
            row = new_row

        for node in row:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)

        return root
