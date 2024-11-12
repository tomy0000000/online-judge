# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        length = len(nums)
        max_length = 0
        flip_used = 0
        for right in range(length):
            if nums[right] == 0:
                flip_used += 1
                while flip_used > k:
                    if nums[left] == 0:
                        flip_used -= 1
                    left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
