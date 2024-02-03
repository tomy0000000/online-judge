# Let n be the length of arr
#
# Time: O(n * k)
# Space: O(n)


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = [0] * len(arr)
        for i in range(k):
            dp[i] = max(arr[: i + 1]) * (i + 1)
        for i in range(k, len(dp)):
            maxi = 0
            for j in range(1, k + 1):
                here = dp[i - j] + max(arr[i - j + 1 : i + 1]) * j
                maxi = max(maxi, here)
            dp[i] = maxi
        return dp[-1]
