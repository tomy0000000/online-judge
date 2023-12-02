# Let n be the length of nums.
#
# Time: O(n * k)
# Space: O(k)
import bisect


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        dp = [0 for _ in range(len(nums) - 1)] + [nums[-1]]
        maxis = []
        for i in range(len(nums) - 1, -1, -1):
            if i + k + 1 < len(nums):
                maxis.remove(dp[i + k + 1])
            maxi = 0 if not maxis else maxis[-1]
            dp[i] = nums[i] + maxi
            bisect.insort(maxis, dp[i])
        return dp[0]
