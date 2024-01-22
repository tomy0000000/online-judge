# Let n be the number of cells in grid
#
# Time: O(n * log(n))
# Space: O(n)

from typing import Optional


class Solution:
    def connected(
        self,
        grid: list[list[int]],
        n: int,
        threshold: int,
        visited: Optional[set[tuple[int, int]]] = None,
        i: Optional[int] = 0,
        j: Optional[int] = 0,
    ) -> bool:
        if not (0 <= i < n and 0 <= j < n):
            return False
        if i == n - 1 and j == n - 1:
            return True
        if grid[i][j] > threshold:
            return False
        visited = set() if not visited else visited
        if (i, j) in visited:
            return False

        visited.add((i, j))
        for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if self.connected(grid, n, threshold, visited, ii, jj):
                return True

        return False

    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        left, right = grid[-1][-1], max(n for row in grid for n in row)
        while left < right:
            mid = (left + right) // 2
            if self.connected(grid, n, mid):
                right = mid
            else:
                left = mid + 1
        return left
