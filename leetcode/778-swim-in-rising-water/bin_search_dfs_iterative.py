# Let n be the number of cells in grid
#
# Time: O(n * log(n))
# Space: O(n)

from collections import deque


class Solution:
    def connected(self, grid: list[list[int]], threshold: int) -> bool:
        if grid[0][0] > threshold:
            return False
        n = len(grid)
        visited = set()
        d = deque([(0, 0)])
        while d:
            i, j = d.popleft()
            visited.add((i, j))
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if not (0 <= ii < n and 0 <= jj < n):
                    continue
                if grid[ii][jj] > threshold:
                    continue
                if ii == n - 1 and jj == n - 1:
                    return True
                if (ii, jj) not in visited and (ii, jj) not in d:
                    d.append((ii, jj))
        return False

    def swimInWater(self, grid: list[list[int]]) -> int:
        left, right = grid[-1][-1], max(n for row in grid for n in row)
        while left < right:
            mid = (left + right) // 2
            if self.connected(grid, mid):
                right = mid
            else:
                left = mid + 1
        return left
