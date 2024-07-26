# Time: O(n^3)
# Space: O(n^2)

from math import inf


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        distance = [[inf for _ in range(n)] for _ in range(n)]

        for i, j, dist in edges:
            distance[i][j] = dist
            distance[j][i] = dist

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(
                        distance[i][j], distance[i][k] + distance[k][j]
                    )

        for i in range(n):
            distance[i][i] = inf

        ans = 0
        mini = inf
        for node, dists in enumerate(distance):
            reachable = sum(1 for d in dists if d <= distanceThreshold)
            if reachable <= mini:
                ans = node
                mini = reachable

        return ans
