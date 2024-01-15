# Let n be the length of matches.
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = set(p for m in matches for p in m)
        loses_c = Counter(m[1] for m in matches)
        return [
            sorted([p for p in players if loses_c[p] == 0]),
            sorted([p for p in players if loses_c[p] == 1]),
        ]
