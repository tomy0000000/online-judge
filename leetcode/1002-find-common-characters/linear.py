# Let n be the length of words
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        chars = set()
        counters = []
        for word in words:
            counters.append(Counter(word))
            chars |= set(word)

        ans = []
        for char in chars:
            for _ in range(min(counter[char] for counter in counters)):
                ans.append(char)

        return ans
