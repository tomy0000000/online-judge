# Let n be the number of cells in heights
#
# Time: O(n * log(n))
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def adjacent_node(self, i: int, j: int, m: int, n: int) -> list[int]:
        res = []
        if i > 0:
            res.append((i - 1, j))
        if j > 0:
            res.append((i, j - 1))
        if i < m - 1:
            res.append((i + 1, j))
        if j < n - 1:
            res.append((i, j + 1))
        return res

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        min_heights = [[float("inf") for _ in range(n)] for _ in range(m)]
        min_heights[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            _, i, j = heappop(heap)
            for ii, jj in self.adjacent_node(i, j, m, n):
                effort = max(min_heights[i][j], abs(heights[ii][jj] - heights[i][j]))
                if effort < min_heights[ii][jj]:
                    min_heights[ii][jj] = effort
                    heappush(heap, (effort, ii, jj))

        return min_heights[-1][-1]
