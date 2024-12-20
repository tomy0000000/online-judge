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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        while queue:
            values = [node.val for node in queue]
            values.reverse()
            for i in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 1:
                    node.val = values[i]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return root
