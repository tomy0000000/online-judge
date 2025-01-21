# Let n be the length of grid
#
# Time: O(n)
# Space: O(1)


class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        left, right = 0, sum(grid[0][1:])
        ans = max(left, right)
        for i in range(n - 1):
            left += grid[1][i]
            right -= grid[0][i + 1]
            ans = min(ans, max(left, right))
        return ans
