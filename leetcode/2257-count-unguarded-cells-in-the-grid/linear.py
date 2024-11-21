# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        blocks = [["" for _ in range(n)] for _ in range(m)]

        for i, j in walls:
            blocks[i][j] = "W"
        for i, j in guards:
            blocks[i][j] = "G"

        for i, j in guards:
            for ii in range(i - 1, -1, -1):
                if blocks[ii][j] in ("W", "G"):
                    break
                blocks[ii][j] = "X"

            for ii in range(i + 1, m):
                if blocks[ii][j] in ("W", "G"):
                    break
                blocks[ii][j] = "X"

            for jj in range(j - 1, -1, -1):
                if blocks[i][jj] in ("W", "G"):
                    break
                blocks[i][jj] = "X"

            for jj in range(j + 1, n):
                if blocks[i][jj] in ("W", "G"):
                    break
                blocks[i][jj] = "X"

        return sum(row.count("") for row in blocks)
