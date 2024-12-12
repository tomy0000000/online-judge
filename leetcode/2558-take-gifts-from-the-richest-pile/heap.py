# Let n be the length of gifts
#
# Time: O(n)
# Space: O(1)

from heapq import heapify, heappop, heappush


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapify(gifts)
        for _ in range(k):
            n = heappop(gifts) * -1
            heappush(gifts, -int(n**0.5))
        return -sum(gifts)
