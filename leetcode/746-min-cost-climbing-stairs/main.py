# Let n be the length of cost.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1 : i + 3])
        return min(cost[:2])
