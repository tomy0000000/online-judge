# Let n be the number of cells in box
#
# Time: O(n)
# Space: O(n)


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            stones = 0
            prev_obstacle = n
            for j in range(n - 1, -1, -1):
                if box[i][j] == ".":
                    continue

                if box[i][j] == "#":
                    stones += 1

                if box[i][j] == "*":
                    box[i][j + 1 : prev_obstacle] = ["."] * (
                        prev_obstacle - j - 1 - stones
                    ) + ["#"] * stones
                    prev_obstacle = j
                    stones = 0

            box[i][:prev_obstacle] = ["."] * (prev_obstacle - stones) + ["#"] * stones

        new_box = [["" for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                new_box[j][m - i - 1] = box[i][j]

        return new_box
