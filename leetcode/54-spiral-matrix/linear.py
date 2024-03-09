class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row_l, row_r, col_l, col_r = -1, len(matrix), -1, len(matrix[0])
        row, col, dir = 0, 0, 0
        res = [matrix[row][col]]
        while row_l + 1 < row_r and col_l + 1 < col_r:
            if dir == 0:
                while col + 1 < col_r:
                    col += 1
                    res.append(matrix[row][col])
                row_l += 1
            elif dir == 1:
                while row + 1 < row_r:
                    row += 1
                    res.append(matrix[row][col])
                col_r -= 1
            elif dir == 2:
                while col - 1 > col_l:
                    col -= 1
                    res.append(matrix[row][col])
                row_r -= 1
            else:
                while row - 1 > row_l:
                    row -= 1
                    res.append(matrix[row][col])
                col_l += 1
            dir = (dir + 1) % 4
        return res
