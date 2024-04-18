# Let n be the number of cells in the grid
#
# Time: O(n)
# Space: O(1)


class Solution:
    def sides(self, grid: list[list[int]], row: int, col: int, i: int, j: int) -> int:
        count = 4
        if 0 <= i - 1 < row and grid[i - 1][j] == 1:
            count -= 1
        if 0 <= i + 1 < row and grid[i + 1][j] == 1:
            count -= 1
        if 0 <= j - 1 < col and grid[i][j - 1] == 1:
            count -= 1
        if 0 <= j + 1 < col and grid[i][j + 1] == 1:
            count -= 1
        return count

    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        return sum(
            self.sides(grid, row, col, i, j)
            for i in range(row)
            for j in range(col)
            if grid[i][j] == 1
        )
