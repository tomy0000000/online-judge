# Time: O(n ^ min{k, n - k})
# Space: O(n ^ min{k, n - k})

import itertools


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return itertools.combinations(range(1, n + 1), k)
