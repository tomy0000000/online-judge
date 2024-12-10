# Let n be the length of s
#
# Time: O(n log n)
# Space: O(n)

from bisect import insort
from collections import Counter, defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        prev = s[0]
        acc = 1
        counter = Counter()
        mountains = defaultdict(list)
        for c in s[1:]:
            counter[c] += 1
            if c == prev:
                acc += 1
            else:
                insort(mountains[prev], acc)
                prev = c
                acc = 1
        insort(mountains[prev], acc)

        ans = -1
        for c, mountain in mountains.items():
            while len(mountain) < 3:
                mountain.insert(0, 0)
            if mountain[-3] == mountain[-1]:
                ans = max(ans, mountain[-1])
            elif mountain[-2] == mountain[-1]:
                ans = max(ans, mountain[-1] - 1)
            elif mountain[-2] == mountain[-1] - 1:
                ans = max(ans, mountain[-1] - 1)
            else:
                ans = max(ans, mountain[-1] - 2)

        return ans if ans != 0 else -1
