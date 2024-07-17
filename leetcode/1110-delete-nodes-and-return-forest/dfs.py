# Let n be the number of nodes in the binary tree.
#
# Time: O(n)
# Space: O(n)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.nodes = {}
        self.parents = {}

    def dfs(self, root: Optional[TreeNode], parent: Optional[TreeNode] = None) -> None:
        if not root:
            return

        self.nodes[root.val] = root
        self.parents[root.val] = parent
        if root.left:
            self.dfs(root.left, root)
        if root.right:
            self.dfs(root.right, root)

    def delNodes(
        self, root: Optional[TreeNode], to_delete: list[int]
    ) -> list[TreeNode]:
        trees = [root]
        self.dfs(root)
        for v in to_delete:
            node = self.nodes[v]
            parent = self.parents[v]

            if node is parent.left:
                parent.left = None
            else:
                parent.right = None

            if node in trees:
                trees.remove(node)
            if node.left:
                trees.append(node.left)
            if node.right:
                trees.append(node.right)
        return trees
