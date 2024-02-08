# Time: O(n * sqrt(n))
# Space: O(n)

from functools import cache


class Solution:
    def __init__(self):
        self.psns = [(n + 1) ** 2 for n in range(int(10000**0.5))]

    @cache
    def numSquares(self, n: int) -> int:
        if n in self.psns:
            return 1

        return 1 + min(self.numSquares(n - psn) for psn in self.psns if psn <= n)
