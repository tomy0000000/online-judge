# Let e be the number of edges
#
# Time: O(e + n)
# Space: O(e + n)

from collections import defaultdict, deque


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        neighbors = defaultdict(set)
        for v1, v2 in edges:
            neighbors[v1].add(v2)
            neighbors[v2].add(v1)

        queue = deque([source])
        visited = set()
        while queue:
            here = queue.popleft()
            if here in visited:
                continue
            visited.add(here)
            if destination in neighbors[here]:
                return True
            for v in neighbors[here]:
                if v not in visited:
                    queue.append(v)

        return False
