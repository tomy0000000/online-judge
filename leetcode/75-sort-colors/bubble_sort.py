# Let n be the length of nums
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
