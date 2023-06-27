# Let n be the length of nums.
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def validate_group(self, group: list[str]):
        presented = set()
        for n in group:
            if n != "." and n in presented:
                return False
            presented.add(n)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Validate each row
        for row in board:
            if not self.validate_group(row):
                return False

        # Validate each column
        for column_index in range(9):
            column = [row[column_index] for row in board]
            if not self.validate_group(column):
                return False

        # Validate each sub-grid
        for row_index in range(0, 9, 3):  # 0, 3, 6
            for col_index in range(0, 9, 3):
                # Construct the sub-grid
                sub_grid = []
                for i in range(3):
                    sub_grid += board[row_index + i][col_index : col_index + 3]

                if not self.validate_group(sub_grid):
                    return False

        return True
