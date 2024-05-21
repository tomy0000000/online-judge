# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from functools import reduce


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        n_count = 2 ** (len(nums) - 1)
        or_sum = reduce(lambda a, b: a | b, nums)
        return or_sum * n_count
