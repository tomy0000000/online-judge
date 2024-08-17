# Let n be the length of values
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        maxi = 0
        prev_best = 0
        for n in values:
            prev_best -= 1
            maxi = max(maxi, n + prev_best)
            prev_best = max(prev_best, n)
        return maxi
