# Let n be the number of cells in the grid.
#
# Time: O(n ^ 2)
# Space: O(n)


from typing import Optional


class Solution:
    m: int
    n: int

    def dfs(
        self,
        grid: list[list[int]],
        here: tuple[int, int],
        visited: Optional[set[int]] = None,
    ) -> int:
        if not visited:
            visited = set()

        i, j = here
        if not (0 <= i < self.m and 0 <= j < self.n):
            return 0
        if here in visited:
            return 0
        if grid[i][j] == 0:
            return 0

        visited.add(here)

        maxi = grid[i][j] + max(
            self.dfs(grid, (i - 1, j), visited),
            self.dfs(grid, (i + 1, j), visited),
            self.dfs(grid, (i, j - 1), visited),
            self.dfs(grid, (i, j + 1), visited),
        )

        visited.remove(here)

        return maxi

    def getMaximumGold(self, grid: list[list[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])

        maxi = 0
        for i in range(self.m):
            for j in range(self.n):
                maxi = max(maxi, self.dfs(grid, (i, j)))

        return maxi
