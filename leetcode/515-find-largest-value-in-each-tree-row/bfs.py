# Let n be the number of nodes in the binary tree
#
# Time: O(n)
# Space: O(n)

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        values = []
        queue = deque([root])
        while queue:
            row = []
            for _ in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(max(row))
        return values
