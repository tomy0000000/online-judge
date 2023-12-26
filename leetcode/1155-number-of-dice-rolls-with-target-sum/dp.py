# Time: O(n * k)
# Space: O(1)

from functools import cache


class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0:
            return 1 if target == 0 else 0
        return sum(
            self.numRollsToTarget(n - 1, k, target - i) for i in range(1, k + 1)
        ) % (10**9 + 7)
