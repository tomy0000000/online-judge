# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = []
        for n in nums:
            insert_index = bisect_left(dp, n)
            if insert_index == len(dp):
                dp.append(n)
            else:
                dp[insert_index] = n
        return len(dp)
