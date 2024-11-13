# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(1)

from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        acc = 0
        for i, n in enumerate(nums):
            left = bisect_left(nums, lower - n)
            right = bisect_right(nums, upper - n)
            if right == len(nums) or upper - n < nums[right]:
                right -= 1
            count = right - left + 1
            if left <= i and i <= right:
                count -= 1
            acc += count
        return acc // 2
