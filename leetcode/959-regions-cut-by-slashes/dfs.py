# Let n be the length of grid
#
# Time: O(n^2)
# Space: O(n^2)


class Solution:
    def dfs(self, grid: list[list[int]], i: int, j: int):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid):
            return
        if grid[i][j] == 1:
            return

        grid[i][j] = 1

        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid) * 3
        dot_grid = [[0 for _ in range(n)] for _ in range(n)]
        for i, row in enumerate(grid):
            i *= 3
            for j, c in enumerate(row):
                j *= 3
                if c == "/":
                    dot_grid[i][j + 2] = 1
                    dot_grid[i + 1][j + 1] = 1
                    dot_grid[i + 2][j] = 1
                elif c == "\\":
                    dot_grid[i][j] = 1
                    dot_grid[i + 1][j + 1] = 1
                    dot_grid[i + 2][j + 2] = 1

        regions = 0
        for i in range(n):
            for j in range(n):
                if dot_grid[i][j] == 0:
                    self.dfs(dot_grid, i, j)
                    regions += 1

        return regions
