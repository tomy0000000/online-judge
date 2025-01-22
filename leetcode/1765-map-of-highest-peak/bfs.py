# Let n be the number of cells in the grid.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1 for _ in range(n)] for _ in range(m)]

        level = 0
        this_level = set(
            (i, j) for i in range(m) for j in range(n) if isWater[i][j] == 1
        )
        while this_level:
            next_level = set()
            for i, j in this_level:
                height[i][j] = level
                for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if not (0 <= ii < m and 0 <= jj < n):
                        continue
                    if (ii, jj) in this_level:
                        continue
                    if (ii, jj) in next_level:
                        continue
                    if height[ii][jj] != -1:
                        continue
                    next_level.add((ii, jj))
            this_level = next_level
            level += 1

        return height
