# Let n be the width and height of the matrix.
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                matrix[i][j] += min(matrix[i + 1][max(j - 1, 0) : min(j + 2, n)])
        return min(matrix[0])
