# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(n)

from bisect import insort


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        sub = [nums[0]]
        max_len = 1
        left = 0
        for right in range(1, len(nums)):
            insort(sub, nums[right])
            while sub[-1] - sub[0] > limit:
                sub.remove(nums[left])
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
