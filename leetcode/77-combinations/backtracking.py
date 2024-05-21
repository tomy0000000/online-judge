# Time: O(n ^ min{k, n - k})
# Space: O(n ^ min{k, n - k})

from typing import Optional


class Solution:
    def combine(
        self,
        n: int,
        k: int,
        comb: Optional[list[int]] = None,
        combs: Optional[list[list[int]]] = None,
    ) -> list[list[int]]:
        if comb is None:
            comb = []
        if combs is None:
            combs = []

        if len(comb) == k:
            combs.append(comb.copy())
            return combs

        for n in range(n, 0, -1):
            comb.append(n)
            self.combine(n - 1, k, comb, combs)
            comb.pop()

        return combs
