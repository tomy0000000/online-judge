# Let n be the number of nodes in the binary tree.
#
# Time: O(n)
# Space: O(log n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: TreeNode, add: int = 0) -> int:
        if not root:
            return 0

        root.val += self.dfs(root.right, add) if root.right else add
        return self.dfs(root.left, root.val) if root.left else root.val

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root
