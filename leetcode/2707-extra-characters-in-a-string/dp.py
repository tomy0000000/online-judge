# Let n be the length of the string s
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        length = len(s)
        dictionary = set(dictionary)

        dp = [0] * (length + 1)
        for i in range(length - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i + 1, length + 1):
                sub = s[i:j]
                if sub in dictionary:
                    dp[i] = min(dp[i], dp[j])

        return dp[0]
