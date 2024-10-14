# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        score = 0
        for _ in range(k):
            n = heappop(heap) * -1
            score += n
            heappush(heap, -ceil(n / 3))
        return score
