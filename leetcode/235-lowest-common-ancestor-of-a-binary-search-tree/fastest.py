# Let n be the length of s.
#
# Time: O(log(n))
# Space: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        cur = root
        while True:
            if cur in (p, q):
                return cur

            p_next = cur.left if p.val < cur.val else cur.right
            q_next = cur.left if q.val < cur.val else cur.right

            if p_next != q_next:
                return cur
            cur = p_next
