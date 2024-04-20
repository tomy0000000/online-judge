# Let n be the number of cells in the land.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def label_land(
        self, land: list[list[int]], row: int, col: int, i: int, j: int
    ) -> list[int]:
        r1, c1, r2, c2 = i, j, i, j
        while r2 + 1 < row and land[r2 + 1][c2] == 1:
            r2 += 1
        while c2 + 1 < col and land[r2][c2 + 1] == 1:
            c2 += 1
        for ii in range(r1, r2 + 1):
            land[ii][c1 : c2 + 1] = [2] * (c2 - c1 + 1)
        return [r1, c1, r2, c2]

    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        row, col = len(land), len(land[0])
        groups = []
        for i in range(row):
            for j in range(col):
                if land[i][j] == 1:
                    groups.append(self.label_land(land, row, col, i, j))
        return groups
