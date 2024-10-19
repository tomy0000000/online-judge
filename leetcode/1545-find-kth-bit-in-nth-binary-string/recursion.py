# Time: O(n)
# Space: O(1)

from functools import cache


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.n_string(n)[k - 1]

    @cache
    def n_string(self, n: int) -> str:
        if n == 1:
            return "0"

        prev = self.n_string(n - 1)
        invert = "".join("1" if c == "0" else "0" for c in prev)
        reverse = invert[::-1]
        return prev + "1" + reverse
