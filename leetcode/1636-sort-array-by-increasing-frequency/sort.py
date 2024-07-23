# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)

from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))
