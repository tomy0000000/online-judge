# Let n be the length of s and m be the length of t.
#
# Time: O(n + m)
# Space: O(1)

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s) - Counter(t)).total()
