# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxi = max(nums)
        maxi_length = 0
        left, right = 0, 0
        while True:
            try:
                left = nums.index(maxi, right)
            except ValueError:
                break
            right = left + 1
            while right < len(nums) and nums[right] == maxi:
                right += 1
            maxi_length = max(maxi_length, right - left)
        return maxi_length
