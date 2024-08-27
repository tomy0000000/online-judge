# Let e be the number of edges.
#
# Time: O(e + n)
# Space: O(e + n)

from collections import deque


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        edges_map = {i: {} for i in range(n)}
        for e, p in zip(edges, succProb):
            n1, n2 = e
            if n2 in edges_map[n1]:
                edges_map[n1][n2] = min(edges_map[n1][n2], p)
            else:
                edges_map[n1][n2] = p
            if n1 in edges_map[n2]:
                edges_map[n2][n1] = min(edges_map[n2][n1], p)
            else:
                edges_map[n2][n1] = p

        visited = {}
        queue = deque([(start_node, 1)])
        while queue:
            n, acc_p = queue.popleft()
            visited[n] = acc_p
            for neighbor, p in edges_map[n].items():
                new_p = acc_p * p
                if neighbor not in visited or visited[neighbor] < new_p:
                    queue.append((neighbor, new_p))
                    visited[neighbor] = new_p

        return visited[end_node] if end_node in visited else 0
