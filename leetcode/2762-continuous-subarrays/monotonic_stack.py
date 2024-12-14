# Let n be the length of nums
#
# Time: O(n ^ 2 * log(n))
# Space: O(n)

from bisect import insort


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        left = 0
        included = []
        ans = 0
        for right in range(len(nums)):
            insort(included, nums[right])
            while included[-1] - included[0] > 2:
                included.remove(nums[left])
                left += 1

            ans += right - left + 1

        return ans
