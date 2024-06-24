# Let n be the length of bloomDay
#
# Time: O(n log n)
# Space: O(1)

from bisect import bisect_left


class Solution:
    def possible(self, bloomDay: list[int], m: int, k: int, limit: int) -> bool:
        bouquet = 0
        flowers = 0
        for day in bloomDay:
            if day > limit:
                flowers = 0
                continue
            flowers += 1
            if flowers == k:
                bouquet += 1
                flowers = 0
            if bouquet == m:
                break
        return bouquet == m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        ans = bisect_left(
            range(0, max(bloomDay) + 1),
            True,
            key=lambda x: self.possible(bloomDay, m, k, x),
        )
        return ans if ans <= max(bloomDay) else -1
