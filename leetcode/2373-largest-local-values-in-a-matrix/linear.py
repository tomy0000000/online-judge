# Let n be the number of cells in the grid.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        mat = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(n):
            for j in range(n):
                for k in range(3):
                    for l in range(3):
                        if i - k < 0 or j - l < 0 or i - k >= n - 2 or j - l >= n - 2:
                            continue
                        mat[i - k][j - l] = max(mat[i - k][j - l], grid[i][j])
        return mat
