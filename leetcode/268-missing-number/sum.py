# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
