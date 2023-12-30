# Let n be the length of nums.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        nums[1] = max(nums[:2])
        for i in range(2, n):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])

        return nums[-1]
