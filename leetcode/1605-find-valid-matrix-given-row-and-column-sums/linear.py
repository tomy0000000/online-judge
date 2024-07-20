# Let n be the number of cells in the matrix.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        row_num, col_num = len(rowSum), len(colSum)
        matrix = [colSum] + [[0 for _ in range(col_num)] for _ in range(row_num - 1)]
        for i in range(row_num - 1):
            total_move = sum(matrix[i]) - rowSum[i]
            moves = matrix[i].copy()
            j = 0
            while total_move:
                if total_move >= moves[j]:
                    total_move -= moves[j]
                else:
                    moves[j] = total_move
                    total_move = 0
                j += 1
            moves[j:] = [0] * (col_num - j)
            for j in range(col_num):
                matrix[i][j] -= moves[j]
                matrix[i + 1][j] += moves[j]
        return matrix
