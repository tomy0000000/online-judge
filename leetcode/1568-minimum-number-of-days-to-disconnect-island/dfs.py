# Let n be the number of cells in the grid.
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    m: int
    n: int

    def mark(
        self, grid: list[list[int]], visited: list[list[bool]], i: int, j: int
    ) -> None:
        visited[i][j] = True
        for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not (0 <= i + ii < self.m and 0 <= j + jj < self.n):
                continue
            if visited[i + ii][j + jj]:
                continue
            if grid[i + ii][j + jj] == 0:
                continue
            self.mark(grid, visited, i + ii, j + jj)

    def num_islands(self, grid: list[list[int]]) -> int:
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        island = 0
        for i in range(self.m):
            for j in range(self.n):
                if visited[i][j]:
                    continue
                if grid[i][j] == 0:
                    continue
                self.mark(grid, visited, i, j)
                island += 1
        return island

    def minDays(self, grid: list[list[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        if self.num_islands(grid) != 1:
            return 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.num_islands(grid) != 1:
                        return 1
                    grid[i][j] = 1

        return 2
