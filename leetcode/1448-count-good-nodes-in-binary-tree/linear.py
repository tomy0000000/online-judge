# Let n be the number of nodes in the tree
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
    def good_nodes_with_max(self, node: Optional[TreeNode], parent_max: int):
        if not node:
            return 0

        new_parent_max = max(parent_max, node.val)
        children_good_nodes = self.good_nodes_with_max(
            node.left, new_parent_max
        ) + self.good_nodes_with_max(node.right, new_parent_max)

        if node.val < parent_max:
            return children_good_nodes
        else:
            return 1 + children_good_nodes

    def goodNodes(self, root: TreeNode) -> int:
        return self.good_nodes_with_max(root, root.val - 1)
