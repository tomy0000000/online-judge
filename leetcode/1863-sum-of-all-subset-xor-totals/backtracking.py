# Let n be the length of nums
#
# Time: O(n)
# Space: O(2 ^ n)

from functools import reduce


class Solution:
    def backtrack(self, nums):
        if not nums:
            return [[]]

        n = nums.pop()
        combs = self.backtrack(nums)
        return [comb + [n] for comb in combs] + combs

    def subsetXORSum(self, nums: list[int]) -> int:
        return sum(reduce(lambda a, b: a ^ b, comb, 0) for comb in self.backtrack(nums))
