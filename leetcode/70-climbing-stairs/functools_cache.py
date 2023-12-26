# Time: O(n)
# Space: O(n)

from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return result
