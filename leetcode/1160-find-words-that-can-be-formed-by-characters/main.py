# Let n be the length of all chars in words, m be the length of chars.
#
# Time: O(n + m)
# Space: O(m)

from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        quota = Counter(chars)
        ans = 0
        for w in words:
            usage = Counter(w)
            for c in quota:
                if usage.pop(c, 0) > quota[c]:
                    break
            else:
                if not usage:
                    ans += len(w)
        return ans
