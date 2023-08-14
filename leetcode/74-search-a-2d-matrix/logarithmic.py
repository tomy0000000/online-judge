# Let m and n be the number of rows and columns of the matrix, respectively.
#
# Time: O(log(m * n))
# Space: O(1)


class Solution:
    def find_row(
        self, matrix: list[list[int]], target: int, row_start: int, row_end: int
    ) -> int:
        if target < matrix[0][0]:
            return 0

        if len(matrix) == 1:
            return 0

        if row_start + 1 >= row_end:
            return row_start if target < matrix[1][0] else row_end

        mid_index = (row_start + row_end) // 2
        mid = matrix[mid_index][0]
        mid_next = (
            matrix[mid_index + 1][0] if mid_index + 1 < len(matrix) else matrix[-1][-1]
        )
        if mid <= target and target < mid_next:
            return mid_index
        elif target < mid:
            return self.find_row(matrix, target, row_start, mid_index)
        else:
            return self.find_row(matrix, target, mid_index, row_end)

    def find_col(self, row: list[int], target: int, start: int, end: int):
        if start + 1 >= end:
            return row[start] == target or row[end] == target
        mid_index = (start + end) // 2
        mid = row[mid_index]
        if mid == target:
            return True
        elif target < mid:
            return self.find_col(row, target, start, mid_index)
        else:
            return self.find_col(row, target, mid_index, end)

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = self.find_row(matrix, target, 0, len(matrix) - 1)
        return self.find_col(matrix[row], target, 0, len(matrix[row]) - 1)
