# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)

from collections import Counter
from typing import Optional


class Solution:
    def find_missing(self, counter: Counter, k: int) -> Optional[str]:
        for c in "abc":
            if counter[c] < k:
                return c

    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter()
        length = len(s)
        for left, c in enumerate(s):
            counter[c] += 1
            if self.find_missing(counter, k) is None:
                break
        else:
            return -1

        mini = left + 1
        right = length
        while left >= 0:
            counter[s[left]] -= 1
            left -= 1

            missing = self.find_missing(counter, k)
            if missing is None:
                mini = min(mini, left + length - right + 1)
                continue

            added = None
            while added != missing:
                right -= 1
                added = s[right]
                counter[added] += 1

            mini = min(mini, left + length - right + 1)

        return mini
