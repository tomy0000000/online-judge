# Let n be the length of s1 + s2
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        return [
            k
            for k in set(c1).symmetric_difference(set(c2))
            if c1[k] <= 1 and c2[k] <= 1
        ]
