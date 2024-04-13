# Let m, n be the number of rows and columns of the matrix.
#
# Time: O(m * n)
# Space: O(1)


class Solution:
    def new_squares(self, squares, new_x_left, new_x_right, row):
        x_range = (new_x_left, new_x_right)

        # Find earliest row
        new_squares = {}
        smallest_y_low = row
        for (x_left, x_right), (y_low, y_top) in squares.items():
            if x_left <= new_x_left and new_x_right <= x_right:
                # New square is inside old square
                smallest_y_low = min(smallest_y_low, y_low)
                continue
            elif x_left < new_x_left < x_right < new_x_right:
                # Overlap on left
                sub_x_range = (new_x_left, x_right)
            elif new_x_left < x_left < new_x_right < x_right:
                # Overlap on right
                sub_x_range = (x_left, new_x_right)
            else:
                continue
            if sub_x_range in new_squares:
                new_squares[sub_x_range][0] = min(new_squares[sub_x_range][0], y_low)
            else:
                new_squares[sub_x_range] = [y_low, row + 1]
        new_squares[x_range] = [smallest_y_low, row + 1]

        # Merge new squares
        for new_range, new_square in new_squares.items():
            if new_range not in squares:
                squares[new_range] = new_square

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        squares = {}
        max_area = 0
        for row_index in range(len(matrix)):
            row = matrix[row_index]
            prev = None
            to_eliminate = set()
            for col_index, cell in enumerate(row):
                if cell == "0":
                    for (x_left, x_right), (y_low, y_top) in squares.items():
                        # Maximum square
                        if x_left <= col_index < x_right:
                            area = (x_right - x_left) * (y_top - y_low)
                            max_area = max(max_area, area)
                            to_eliminate.add((x_left, x_right))

                    # New possible squares
                    if prev is not None:
                        self.new_squares(squares, prev, col_index, row_index)
                    prev = None
                elif cell == "1" and prev is None:
                    prev = col_index

            # New possible squares
            if prev is not None:
                self.new_squares(squares, prev, len(row), row_index)

            # Eliminate squares
            for key in to_eliminate:
                squares.pop(key)

            # Extend squares
            for x_range in squares:
                squares[x_range][-1] = row_index + 1

        # Remained maximum square
        for (x_left, x_right), (y_low, y_top) in squares.items():
            area = (x_right - x_left) * (y_top - y_low)
            max_area = max(max_area, area)

        return max_area
