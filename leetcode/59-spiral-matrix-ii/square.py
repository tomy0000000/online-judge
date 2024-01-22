# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        matrix[0] = list(range(1, n + 1))

        next_change = []
        for k in range(1, n):
            next_change.append(k)
            next_change.append(k)

        i, j, dir = 1, n - 1, 1
        for d in range(n + 1, n**2 + 1):
            matrix[i][j] = d
            next_change[-1] -= 1

            if next_change[-1] == 0:
                next_change.pop()
                dir = (dir + 1) % 4

            if dir == 0:  # right
                j += 1
            if dir == 1:  # down
                i += 1
            if dir == 2:  # left
                j -= 1
            if dir == 3:  # up
                i -= 1

        return matrix
