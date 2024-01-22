# Let n be the number of elements in the matrix.
#
# Time: O(n)
# Space: O(n)

from collections import defaultdict
from typing import Optional


class Solution:
    def find_longest(
        self, edges: list[list[set[tuple[int, int]]]], starter: tuple[int, int]
    ) -> int:
        stack = self.topo_sort(edges, starter)
        dist = defaultdict(int)
        dist[starter] = 1

        while stack:
            i, j = stack.pop()
            for ii, jj in edges[i][j]:
                dist[(ii, jj)] = max(dist[(ii, jj)], dist[(i, j)] + 1)

        return max(dist.values())

    def topo_sort(
        self,
        edges: list[list[set[tuple[int, int]]]],
        current: tuple[int, int],
        stack: Optional[list[tuple[int, int]]] = None,
        visited: Optional[set[tuple[int, int]]] = None,
    ) -> list[tuple[int, int]]:
        visited = set() if visited is None else visited
        stack = [] if stack is None else stack

        i, j = current
        visited.add((i, j))
        for ii, jj in edges[i][j]:
            if (ii, jj) not in visited:
                self.topo_sort(edges, (ii, jj), stack, visited)
        stack.append((i, j))

        return stack

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        edges = [[set() for _ in range(n)] for _ in range(m)]
        starters = set((i, j) for i in range(m) for j in range(n))
        for i in range(m):
            for j in range(n):
                for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if ii < 0 or ii >= m or jj < 0 or jj >= n:
                        continue
                    if matrix[ii][jj] > matrix[i][j]:
                        edges[i][j].add((ii, jj))
                        starters.discard((ii, jj))

        max_dist = 0
        for starter in starters:
            max_dist = max(max_dist, self.find_longest(edges, starter))
        return max_dist
