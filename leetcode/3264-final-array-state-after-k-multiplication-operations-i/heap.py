# Let n be the length of nums
#
# Time: O(n + k)
# Space: O(n)

from heapq import heapify, heappop, heappush


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            n, i = heappop(heap)
            n *= multiplier
            nums[i] = n
            heappush(heap, (n, i))
        return nums
