# Let n be the length of nums
#
# Time: O(n log k)
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            heappush(heap, n)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)
