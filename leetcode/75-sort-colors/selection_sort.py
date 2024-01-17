# Let n be the length of nums
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            argmin = min(range(i, len(nums)), key=lambda x: nums[x])
            nums[i], nums[argmin] = nums[argmin], nums[i]
