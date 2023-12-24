# Let m be the number of rows and n be the number of columns.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def bounded(self, i: int, j: int, m: int, n: int):
        return -1 < i < m and -1 < j < n

    def mark(
        self,
        grid: list[list[str]],
        visited: list[list[bool]],
        i: int,
        j: int,
        m: int,
        n: int,
    ) -> None:
        visited[i][j] = True
        for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not self.bounded(i + ii, j + jj, m, n):
                continue
            if visited[i + ii][j + jj]:
                continue
            if grid[i + ii][j + jj] == "0":
                continue
            self.mark(grid, visited, i + ii, j + jj, m, n)

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        island = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if grid[i][j] == "0":
                    continue
                self.mark(grid, visited, i, j, m, n)
                island += 1
        return island
