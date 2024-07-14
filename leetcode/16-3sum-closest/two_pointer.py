# Let n be the length of nums
#
# Time: O(n^2)
# Space: O(n)

from math import inf


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        optimal = inf
        for i, n in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = n + nums[left] + nums[right]

                if summ == target:
                    return target
                if summ < target:
                    left += 1
                else:
                    right -= 1

                if abs(target - summ) < abs(target - optimal):
                    optimal = summ
        return optimal
