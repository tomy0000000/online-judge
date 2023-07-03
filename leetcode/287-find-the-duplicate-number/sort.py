# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1):
            # for j in range(i + 1, len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]
