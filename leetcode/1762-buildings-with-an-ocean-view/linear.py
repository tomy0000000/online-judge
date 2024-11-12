# Let n be the length of heights
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        queue = deque()
        maxi = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxi:
                queue.appendleft(i)
                maxi = heights[i]
        return list(queue)
