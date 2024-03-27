# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        ans = 0
        pro = 1
        left = 0
        for right in range(len(nums)):
            pro *= nums[right]
            if pro >= k:
                while pro >= k and left <= right:
                    pro /= nums[left]
                    left += 1
            ans += right - left + 1
        return ans
