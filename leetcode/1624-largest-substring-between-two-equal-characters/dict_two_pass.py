# Let n be the length of s
#
# Time: O(n)
# Space: O(1)

from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        maxi = -1
        for c, p in pos.items():
            dist = p[-1] - p[0] - 1
            maxi = max(maxi, dist)
        return maxi
