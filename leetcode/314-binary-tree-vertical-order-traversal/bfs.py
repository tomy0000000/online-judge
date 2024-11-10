# Let n be the number of nodes
#
# Time: O(n)
# Space: O(n)

from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        queue = deque([(root, 0)])
        column_dict = defaultdict(list)
        while queue:
            node, column = queue.popleft()
            column_dict[column].append(node.val)
            if node.left is not None:
                queue.append((node.left, column - 1))
            if node.right is not None:
                queue.append((node.right, column + 1))

        return [
            tup[1] for tup in sorted((col, group) for col, group in column_dict.items())
        ]
