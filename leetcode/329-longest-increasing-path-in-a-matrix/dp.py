# Let n be the number of elements in the matrix.
#
# Time: O(n)
# Space: O(n)

from functools import cache


class Solution:
    matrix: list[list[int]]
    dp: list[list[int]]
    m: int
    n: int

    @cache
    def update_dist(self, i: int, j: int) -> int:
        candidates = [0]
        for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if ii < 0 or ii >= self.m or jj < 0 or jj >= self.n:
                continue
            if self.matrix[ii][jj] >= self.matrix[i][j]:
                continue
            candidates.append(self.update_dist(ii, jj))
        self.dp[i][j] = 1 + max(candidates)
        return self.dp[i][j]

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.update_dist(i, j)

        return max(max(self.dp, key=max))
