# Let n be the number of nodes in the binary tree
#
# Time: O(n * log(n))
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
    def minSwapsToSort(self, arr):
        n = len(arr)
        indexedArr = [(arr[i], i) for i in range(n)]
        indexedArr.sort()
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexedArr[i][1] == i:
                continue

            cycleSize = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = indexedArr[j][1]
                cycleSize += 1

            if cycleSize > 1:
                swaps += cycleSize - 1

        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        swap = 0
        queue = deque([root])
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            swap += self.minSwapsToSort(values)
        return swap
