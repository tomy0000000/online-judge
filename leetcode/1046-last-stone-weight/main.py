# Let n be the number of stones.
#
# Time: O(n)
# Space: O(1)

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            x, y = -x, -y

            if y > x:
                new = y - x
                heapq.heappush(stones, -new)

        return -stones[0] if stones else 0
