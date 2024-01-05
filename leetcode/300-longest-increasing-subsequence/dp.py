# Let n be the length of nums
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] + [0 for _ in range(len(nums) - 1)]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > dp[i]:
                    dp[i] = dp[j]
            dp[i] += 1
        return max(dp)
