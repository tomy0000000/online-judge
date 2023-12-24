# Let n be the length of nums.
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        c = Counter(nums)
        return {v: k for k, v in c.items()}[1]
