# Let n be the length of matrix
#
# Time: O(n)
# Space: O(n)

from collections import Counter
from functools import cache


class Solution:
    @cache
    def min_bin(self, bin_str: str) -> int:
        inverted = "".join("1" if b == "0" else "0" for b in bin_str)
        return min(int(bin_str, base=2), int(inverted, base=2))

    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        c = Counter()
        for row in matrix:
            bin_str = "".join(map(str, row))
            c[self.min_bin(bin_str)] += 1

        return max(c.values())
