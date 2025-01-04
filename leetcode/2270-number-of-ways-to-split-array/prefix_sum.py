# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)
        valid = 0
        for n in nums[:-1]:
            left += n
            right -= n
            if left >= right:
                valid += 1
        return valid
