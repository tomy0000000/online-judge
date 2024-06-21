# Let n be the length of bloomDay
#
# Time: O(n log n)
# Space: O(1)


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
        left = 0
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if self.possible(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left if self.possible(bloomDay, m, k, left) else -1
