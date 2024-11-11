# Let n be the number of cells in grid
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    DIR = [
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        visited = set()
        queue = deque([(0, 0, 1)])
        while queue:
            x, y, step = queue.popleft()
            visited.add((x, y))
            if x == n - 1 and y == n - 1:
                return step
            for x_delta, y_delta in self.DIR:
                xx, yy = x + x_delta, y + y_delta
                if xx < 0 or n <= xx:
                    continue
                if yy < 0 or n <= yy:
                    continue
                if (xx, yy) in visited:
                    continue
                if grid[xx][yy] == 0:
                    visited.add((xx, yy))
                    queue.append((xx, yy, step + 1))
        return -1
