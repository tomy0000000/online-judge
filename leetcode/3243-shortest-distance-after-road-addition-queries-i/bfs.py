# Let m be the length of queries
#
# Time: O(n * m)
# Space: O(n + m)

from collections import deque


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        self.paths = {i: set([i + 1]) for i in range(n)}
        res = []
        for start, end in queries:
            self.paths[start].add(end)

            queue = deque([(0, 0)])
            visited = set([0])
            abort = False
            while queue:
                node, steps = queue.popleft()
                for next_node in self.paths[node]:
                    if next_node == n - 1:
                        res.append(steps + 1)
                        abort = True
                        break
                    if next_node not in queue and next_node not in visited:
                        queue.append((next_node, steps + 1))
                        visited.add(next_node)
                if abort:
                    break

        return res
