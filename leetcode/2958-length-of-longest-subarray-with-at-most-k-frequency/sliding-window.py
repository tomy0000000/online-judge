# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        c = Counter()
        left = 0
        maxi = 0
        for right in range(len(nums)):
            c[nums[right]] += 1
            if c[nums[right]] > k:
                while c[nums[right]] > k and left < right:
                    c[nums[left]] -= 1
                    left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
