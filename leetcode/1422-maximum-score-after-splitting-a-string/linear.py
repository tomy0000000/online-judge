# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def maxScore(self, s: str) -> int:
        maxi = 0
        for i in range(1, len(s)):
            score = s[:i].count("0") + s[i:].count("1")
            maxi = max(maxi, score)
        return maxi
