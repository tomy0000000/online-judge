# Let n be the length of deck, m be the number of unique cards
#
# Time: O(n + m log n)
# Space: O(m)

from collections import Counter
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        return gcd(*Counter(deck).values()) != 1
