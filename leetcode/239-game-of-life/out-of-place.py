# Let the board be n x m.
#
# Time: O(n × m)
# Space: O(n × m)


class Solution:
    def get_neighbors(self, board: list[list[int]], i: int, j: int):
        neighbors = []
        max_row = len(board) - 1
        max_col = len(board[0]) - 1

        for row in (0, 1, -1):
            if i + row < 0 or max_row < i + row:  # Skip out of bounds.
                continue
            for col in (0, 1, -1):
                if j + col < 0 or max_col < j + col:  # Skip out of bounds.
                    continue
                if row == 0 and col == 0:  # Skip the current cell.
                    continue
                neighbors.append(board[i + row][j + col])

        return neighbors

    def gameOfLife(self, board: list[list[int]]) -> None:
        new_board = [[0] * len(row) for row in board]

        # Compute the next state.
        for row in range(len(new_board)):
            for col in range(len(new_board[row])):
                # Count the live neighbors.
                neighbors = self.get_neighbors(board, row, col)
                live_neighbors = neighbors.count(1)

                # Toggle the alive/dead state of the cell.
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_board[row][col] = 0
                elif board[row][col] == 0 and live_neighbors == 3:
                    new_board[row][col] = 1
                else:
                    new_board[row][col] = board[row][col]

        # board = new_board
        for row in range(len(new_board)):
            for col in range(len(new_board[row])):
                board[row][col] = new_board[row][col]
