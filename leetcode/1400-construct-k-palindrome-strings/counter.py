# Let n be the length of s
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        counter = Counter(s)
        odd_count = sum(1 for c in counter if counter[c] % 2 == 1)
        if odd_count > k:
            return False

        return True
