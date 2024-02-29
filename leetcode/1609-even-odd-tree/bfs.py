# Let n be the number of nodes in the tree.
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False

        queue = deque([root])
        dec = True
        while queue:
            level_queue = deque()
            while queue:
                node = queue.popleft()
                for child in (node.left, node.right):
                    if not child:
                        continue
                    level_queue.append(child)
            prev = None
            while level_queue:
                node = level_queue.popleft()
                if dec:
                    if node.val % 2 == 1:
                        return False
                    if prev and node.val >= prev:
                        return False
                else:
                    if node.val % 2 == 0:
                        return False
                    if prev and node.val <= prev:
                        return False
                prev = node.val
                queue.append(node)
            dec = not dec
        return True
