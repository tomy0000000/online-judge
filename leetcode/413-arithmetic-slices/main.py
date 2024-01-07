# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        prev = 0
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                ans += prev + 1
                prev += 1
            else:
                prev = 0
        return ans
