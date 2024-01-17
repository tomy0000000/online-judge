# Let n be the length of arr.
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences = Counter(arr).values()
        return len(set(occurrences)) == len(occurrences)
