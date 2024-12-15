# Let n be the length of classes
#
# Time: O(n)
# Space: O(n)

from heapq import heapify, heappop, heappush


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        heap = [(-((p + 1) / (t + 1) - p / t), p, t) for p, t in classes]
        heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heappop(heap)
            p += 1
            t += 1
            heappush(heap, (-((p + 1) / (t + 1) - p / t), p, t))

        return sum(p / t for _, p, t in heap) / len(heap)
