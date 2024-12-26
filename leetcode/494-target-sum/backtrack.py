# Let n be the length of nums
#
# Time: O(2^n)
# Space: O(n)

from functools import cache


class Solution:
    @cache
    def find_target_sum_ways(
        self, nums: tuple[int], target: int, index: int = 0, summ: int = 0
    ) -> int:
        if index == len(nums):
            return int(summ == target)

        add = self.find_target_sum_ways(nums, target, index + 1, summ + nums[index])
        sub = self.find_target_sum_ways(nums, target, index + 1, summ - nums[index])
        return add + sub

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        return self.find_target_sum_ways(tuple(nums), target)
