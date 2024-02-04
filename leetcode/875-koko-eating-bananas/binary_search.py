# Let n be the length of piles
#
# Time: O(n * log(max(piles)))
# Space: O(1)


class Solution:
    def hours(self, piles: list[int], speed: int) -> int:
        return sum(b // speed + 1 if b % speed > 0 else b // speed for b in piles)

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            if self.hours(piles, mid) > h:
                left = mid + 1
            else:
                right = mid
        return left
