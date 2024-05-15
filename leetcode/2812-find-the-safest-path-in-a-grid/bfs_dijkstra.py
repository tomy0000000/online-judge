# Let n be the number of cells in the grid.
#
# Time: O(n ^ 2)
# Space: O(1)


from collections import deque
from heapq import heappop, heappush
from math import inf


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)

        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    queue.append((i, j))
                else:
                    grid[i][j] = inf

        while queue:
            i, j = queue.popleft()
            s = grid[i][j]
            for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] > s + 1:
                    grid[ii][jj] = s + 1
                    queue.append((ii, jj))

        heap = [(-grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        while heap:
            safe, i, j = heappop(heap)
            safe *= -1

            if i == n - 1 and j == n - 1:
                return safe

            for loc in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                ii, jj = loc
                if ii < 0 or ii >= n or jj < 0 or jj >= n or loc in visited:
                    continue
                visited.add(loc)
                heappush(heap, (-min(safe, grid[ii][jj]), ii, jj))

        return -1
