# Let n be the length of word1 and m be the length of word2.
#
# Time: O(n + m)
# Space: O(1)

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        cc1 = Counter(c1.values())
        cc2 = Counter(c2.values())
        return c1.keys() == c2.keys() and cc1 == cc2
