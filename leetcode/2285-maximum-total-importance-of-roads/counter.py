# Let m be the length of roads
#
# Time: O(n log n + m)
# Space: O(n)

from collections import Counter


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        c = Counter()
        for i in range(n):
            c[i] = 0
        for n1, n2 in roads:
            c[n1] += 1
            c[n2] += 1
        return sum(i * n for i, n in enumerate(sorted(c.values()), 1))
