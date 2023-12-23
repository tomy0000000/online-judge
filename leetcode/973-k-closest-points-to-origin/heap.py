# Let n be the length of points.
#
# Time: O(n log k)
# Space: O(n)

from heapq import heappush, heappushpop


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(heap) == k:
                heappushpop(heap, (dist, x, y))
            else:
                heappush(heap, (dist, x, y))
        return [[x, y] for (_, x, y) in heap]
