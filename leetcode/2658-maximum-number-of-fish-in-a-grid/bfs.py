# Let n be the number of cells in the grid.
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def catch(self, grid: list[list[int]], i: int, j: int) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        queue = deque([(i, j)])
        while queue:
            ii, jj = queue.popleft()
            total += grid[ii][jj]
            grid[ii][jj] = -1
            for iii, jjj in ((ii, jj + 1), (ii, jj - 1), (ii + 1, jj), (ii - 1, jj)):
                if not (0 <= iii < m and 0 <= jjj < n):
                    continue

                if (iii, jjj) in queue:
                    continue

                if grid[iii][jjj] <= 0:
                    continue

                queue.append((iii, jjj))

        return total

    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_catch = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= 0:
                    continue
                max_catch = max(max_catch, self.catch(grid, i, j))

        return max_catch
