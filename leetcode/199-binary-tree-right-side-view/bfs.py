# Let n be the number of nodes in the tree
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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        queue = deque([(root, 0)])
        ans = []

        while queue:
            node, level = queue.popleft()

            if not queue or queue[0][1] != level:
                ans.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return ans
