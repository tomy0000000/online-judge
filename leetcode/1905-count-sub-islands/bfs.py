# Let n be the total number of cells in grid1 and grid2
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    m: int
    n: int

    def bounded(self, i: int, j: int) -> bool:
        return 0 <= i < self.m and 0 <= j < self.n

    def get_island(
        self, grid: list[list[int]], visited: list[list[bool]], i: int, j: int
    ) -> set[tuple[int, int]]:
        island = set()
        queue = deque([(i, j)])
        while queue:
            ii, jj = queue.popleft()
            island.add((ii, jj))
            visited[ii][jj] = True
            for dir_i, dir_j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                iii, jjj = ii + dir_i, jj + dir_j
                if not self.bounded(iii, jjj):
                    continue
                if grid[iii][jjj] == 0:
                    continue
                if visited[iii][jjj]:
                    continue
                if (iii, jjj) in queue:
                    continue
                if (iii, jjj) in island:
                    continue
                queue.append((iii, jjj))
        return island

    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        self.m, self.n = len(grid1), len(grid1[0])
        islands = []
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if visited[i][j]:
                    continue
                if grid2[i][j] == 0:
                    visited[i][j] = True
                    continue
                islands.append(self.get_island(grid2, visited, i, j))

        sub = 0
        for island in islands:
            for i, j in island:
                if grid1[i][j] == 0:
                    break
            else:
                sub += 1

        return sub
