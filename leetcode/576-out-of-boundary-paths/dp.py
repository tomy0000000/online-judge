# Let k be maxMove
#
# Time: O(m * n * k)
# Space: O(m * n * k)

from functools import cache


class Solution:
    @cache
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        if (
            maxMove == 0
            or startRow < 0
            or startRow >= m
            or startColumn < 0
            or startColumn >= n
        ):
            return 0

        if maxMove == 1:
            out = 0
            if startRow == 0:
                out += 1
            if startRow == m - 1:
                out += 1
            if startColumn == 0:
                out += 1
            if startColumn == n - 1:
                out += 1
            return out

        return (
            self.findPaths(m, n, 1, startRow, startColumn)
            + self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
            + self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
            + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
            + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
        ) % (10**9 + 7)
