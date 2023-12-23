# Let n be the length of points.
#
# Time: O(n log n)
# Space: O(n)

from heapq import heappush


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        heap = []
        for i, (px, py) in enumerate(points):
            if px != x and py != y:
                continue
            dist = abs(x - px) + abs(y - py)
            heappush(heap, (dist, i))
        if not heap:
            return -1
        return heap[0][1]
