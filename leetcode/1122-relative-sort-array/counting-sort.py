# Let n be the length of arr1
#
# Time: O(n log n)
# Space: O(n)

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        c = Counter(arr1)
        ans = []
        for n in arr2:
            ans += [n for _ in range(c.pop(n))]
        remains = sorted(c.keys())
        for n in remains:
            ans += [n for _ in range(c.pop(n))]
        return ans
