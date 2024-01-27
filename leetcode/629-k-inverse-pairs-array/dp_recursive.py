# Time: O(n * k)
# Space: O(n * k)

from functools import cache


class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return 1
        if n == 1:
            return 0

        return (
            self.kInversePairs(n, k - 1)
            + self.kInversePairs(n - 1, k)
            - self.kInversePairs(n - 1, k - n)
        ) % (10**9 + 7)
