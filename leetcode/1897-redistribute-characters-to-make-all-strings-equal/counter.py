# Let n be the length of all words combined.
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)
        counter = Counter("".join(words))
        for char, count in counter.items():
            if count % n != 0:
                return False
        return True
