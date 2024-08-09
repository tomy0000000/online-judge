# Let n be the number of rows and m be the number of columns in the grid.
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def is_magic(self, grid: list[list[int]]) -> bool:
        numbers = set(n for row in grid for n in row)
        if numbers != set(range(1, 10)):
            return False

        summ = sum(grid[0])

        for row in grid:
            if sum(row) != summ:
                return False

        for i in range(3):
            if sum(row[i] for row in grid) != summ:
                return False

        if grid[0][0] + grid[1][1] + grid[2][2] != summ:
            return False
        if grid[0][2] + grid[1][1] + grid[2][0] != summ:
            return False

        return True

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid) - 2, len(grid[0]) - 2
        count = 0
        for i in range(rows):
            for j in range(cols):
                if self.is_magic(
                    [
                        grid[i][j : j + 3],
                        grid[i + 1][j : j + 3],
                        grid[i + 2][j : j + 3],
                    ]
                ):
                    count += 1

        return count
