# Let n be the length of nums
#
# Time: O(n^2 * log(n))
# Space: O(n)

from bisect import bisect_left
from math import inf


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        min_diff = inf
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                optimal = target - nums[i] - nums[j]

                k = bisect_left(nums, optimal, j + 1, length)
                if k >= length:
                    # Out of bound, back to end
                    diff = nums[k - 1] - optimal
                elif nums[k] == optimal:
                    return target
                elif j < k - 1:
                    # Prefer left element if it is closer
                    left_diff = optimal - nums[k - 1]
                    right_diff = nums[k] - optimal
                    diff = -left_diff if left_diff < right_diff else right_diff
                else:
                    diff = nums[k] - optimal

                if abs(diff) < abs(min_diff):
                    min_diff = diff
        return target + min_diff
