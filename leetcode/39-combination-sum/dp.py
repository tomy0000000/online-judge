# Let n be the length of candidates, m be the target value
#
# Time: O(n log n + n * m)
# Space: O(m)

from collections import defaultdict


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        table = defaultdict(list)

        for c in candidates:
            for t in range(target + 1):
                if c == t:
                    table[t].append([c])
                elif t - c in table:
                    for combination in table[t - c]:
                        table[t].append(combination + [c])

        return table[target]
