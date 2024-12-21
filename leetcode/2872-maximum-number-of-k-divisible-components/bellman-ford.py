# Time: O(n)
# Space: O(n)

from collections import defaultdict, deque


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        edge_dict = defaultdict(set)
        edge_nodes = set()
        for s, e in edges:
            edge_dict[s].add(e)
            edge_dict[e].add(s)
            for n in (s, e):
                if len(edge_dict[n]) == 1:
                    edge_nodes.add(n)
                else:
                    edge_nodes.discard(n)

        comp = 1
        queue = deque(edge_nodes)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not edge_dict[node]:
                    continue
                neighbor = next(iter(edge_dict[node]))

                if values[node] % k == 0:
                    comp += 1
                else:
                    values[neighbor] += values[node]
                edge_dict[neighbor].remove(node)

                if len(edge_dict[neighbor]) == 1:
                    queue.append(neighbor)

        return comp
