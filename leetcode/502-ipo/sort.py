# Let n be the length of profits and capital
#
# Time: O(n log n)
# Space: O(n)

from bisect import insort
from collections import defaultdict


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        projects = defaultdict(list)
        for p, c in zip(profits, capital):
            insort(projects[c], p)

        levels = sorted(projects, reverse=True)
        candidates = []
        cap = w
        for _ in range(k):
            while levels and levels[-1] <= cap:
                for p in projects[levels.pop()]:
                    insort(candidates, p)

            if not candidates:
                break
            cap += candidates.pop()

        return cap
