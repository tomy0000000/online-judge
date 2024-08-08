# Let n be rows * cols.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        x, y = rStart, cStart
        path = [[rStart, cStart]]
        step = 0
        while len(path) < rows * cols:
            move = (step + 2) // 2
            direction = ("R", "D", "L", "U")[step % 4]

            for _ in range(move):
                if direction == "R":
                    y += 1
                elif direction == "L":
                    y -= 1
                elif direction == "D":
                    x += 1
                elif direction == "U":
                    x -= 1
                if 0 <= x < rows and 0 <= y < cols:
                    path.append([x, y])

            step += 1
        return path
