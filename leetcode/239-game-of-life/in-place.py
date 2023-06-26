# Let the board be n x m.
#
# Time: O(n × m)
# Space: O(n × m)


class Solution:
    def increment_neighbors(self, board: list[list[int]], i: int, j: int) -> None:
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
                board[i + row][j + col] += 1

    def live_neighbors_board(self, board: list[list[int]]) -> list[list[int]]:
        neighbors_board = [[0] * len(row) for row in board]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    # Increment the live neighbors on neighbors cell.
                    self.increment_neighbors(neighbors_board, row, col)
        return neighbors_board

    def gameOfLife(self, board: list[list[int]]) -> None:
        # Create a board of live neighbor counts.
        neighbors_board = self.live_neighbors_board(board)

        for row in range(len(board)):
            for col in range(len(board[row])):
                live_neighbors = neighbors_board[row][col]

                # Toggle the alive/dead state of the cell.
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
