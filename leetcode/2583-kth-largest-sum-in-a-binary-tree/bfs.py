# Let n be the number of nodes in the tree
#
# Time: O(n log k)
# Space: O(k)

from collections import deque
from heapq import heappop, heappush, heappushpop
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = deque([(root, 1)])
        current_level = 1
        acc = 0
        while queue:
            node, level = queue.popleft()

            if level == current_level:
                acc += node.val
            else:
                if len(heap) == k:
                    heappushpop(heap, acc)
                else:
                    heappush(heap, acc)
                acc = node.val
                current_level = level

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        if len(heap) == k:
            heappushpop(heap, acc)
        else:
            heappush(heap, acc)

        return heappop(heap) if len(heap) == k else -1
