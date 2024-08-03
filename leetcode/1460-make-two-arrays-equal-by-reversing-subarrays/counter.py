# Let n be the length arr
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)
