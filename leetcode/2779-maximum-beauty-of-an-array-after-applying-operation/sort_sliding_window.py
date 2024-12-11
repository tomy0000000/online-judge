# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        maxi = 0
        left = 0
        for right in range(length):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
