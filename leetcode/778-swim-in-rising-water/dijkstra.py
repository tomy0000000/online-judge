# Let n be the number of cells in grid
#
# Time: O(n * log(n))
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        min_grid = [[float("inf") for _ in range(n)] for _ in range(n)]
        min_grid[0][0] = grid[0][0]

        heap = [(min_grid[0][0], 0, 0)]
        while heap:
            _, i, j = heappop(heap)
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if not (0 <= ii < n and 0 <= jj < n):
                    continue
                earliest = max(grid[ii][jj], min_grid[i][j])
                if earliest < min_grid[ii][jj]:
                    min_grid[ii][jj] = earliest
                    heappush(heap, (earliest, ii, jj))

        return min_grid[-1][-1]
