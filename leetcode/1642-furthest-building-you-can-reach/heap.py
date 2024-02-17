# Let n be the length of heights
#
# Time: O(n)
# Space: O(n)

from heapq import heappush, heappushpop


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        diffs = [heights[i] - heights[i - 1] for i in range(1, len(heights))]
        heap = []
        for i, d in enumerate(diffs):
            if d <= 0:
                continue

            if len(heap) < ladders:
                heappush(heap, d)
                continue

            remove = heappushpop(heap, d)
            if remove > bricks:
                return i

            bricks -= remove

        return len(diffs)
