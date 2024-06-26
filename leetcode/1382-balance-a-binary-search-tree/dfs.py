# Let n be the number of nodes in the input tree.
#
# Time: O(n log n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: TreeNode) -> list[int]:
        val = []
        if not root:
            return val

        if root.left:
            val += self.dfs(root.left)
        val.append(root.val)
        if root.right:
            val += self.dfs(root.right)

        return val

    def construct(self, val: list[int]) -> TreeNode:
        length = len(val)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(val[0])
        if length == 2:
            return TreeNode(val[0], right=TreeNode(val[1]))
        if length == 3:
            return TreeNode(val[1], left=TreeNode(val[0]), right=TreeNode(val[2]))

        mid = length // 2
        return TreeNode(
            val[mid],
            left=self.construct(val[:mid]),
            right=self.construct(val[mid + 1 :]),
        )

    def balanceBST(self, root: TreeNode) -> TreeNode:
        val = self.dfs(root)
        return self.construct(val)
