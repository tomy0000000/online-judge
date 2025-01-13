# Let n be the length of s
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        for c, count in counter.items():
            counter[c] = 2 if count % 2 == 0 else 1
        return counter.total()
