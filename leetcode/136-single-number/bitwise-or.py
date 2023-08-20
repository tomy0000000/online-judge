# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = 0
        for i in nums:
            n ^= i

        return n
