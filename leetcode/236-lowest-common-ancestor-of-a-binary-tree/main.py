# Let n be the length of s.
#
# Time: O(log(n))
# Space: O(log(n))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def resolve_path(self, root: TreeNode, node: TreeNode, path: list[TreeNode]):
        path.append(root)
        if root.val == node.val:
            return path
        if root.left:
            l_path = self.resolve_path(root.left, node, path)
            if l_path:
                return l_path
        if root.right:
            r_path = self.resolve_path(root.right, node, path)
            if r_path:
                return r_path
        path.pop()
        return None

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        p_path = self.resolve_path(root, p, [])
        q_path = self.resolve_path(root, q, [])

        for i, (p_n, q_n) in enumerate(zip(p_path, q_path)):
            if p_n != q_n:
                return p_path[i - 1]

        if len(p_path) < len(q_path):
            return p_path[-1]
        else:
            return q_path[-1]
