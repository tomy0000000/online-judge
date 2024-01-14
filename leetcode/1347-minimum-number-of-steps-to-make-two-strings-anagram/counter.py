# Let n be the length of s and m be the length of t.
#
# Time: O(n + m)
# Space: O(1)

from collections import Counter
from string import ascii_lowercase


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        st = Counter(t)
        diff = 0
        for c in ascii_lowercase:
            diff += abs(sc[c] - st[c])
        return diff // 2
