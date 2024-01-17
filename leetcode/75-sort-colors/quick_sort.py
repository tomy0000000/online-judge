# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(1)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        nums.clear()
        nums.extend(self.sortColors(left) + middle + self.sortColors(right))
        return nums
