# Let n be the number of nodes in the tree
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        queue = [root]
        ans = []
        root.level = 0

        while queue:
            node = queue.pop(0)
            level = node.level
            while len(ans) <= level:
                ans.append([])
            ans[level].append(node.val)

            if node.left:
                node.left.level = level + 1
                queue.append(node.left)
            if node.right:
                node.right.level = level + 1
                queue.append(node.right)

        return ans
