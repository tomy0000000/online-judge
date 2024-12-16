# Let n be the length of adjacentPairs
#
# Time: O(n)
# Space: O(n)

from collections import defaultdict, deque


class Solution:
    def remove_edge(
        self, edges: defaultdict[int, list[int]], node: int, neighbor: int
    ) -> None:
        edges[node].remove(neighbor)
        if not edges[node]:
            edges.pop(node)

    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        edges = defaultdict(list)
        for i, j in adjacentPairs:
            edges[i].append(j)
            edges[j].append(i)

        node, neighbors = edges.popitem()
        q = deque([neighbors[0], node])
        self.remove_edge(edges, neighbors[0], node)
        if len(neighbors) > 1:
            q.append(neighbors[1])
            self.remove_edge(edges, neighbors[1], node)

        while edges:
            left, right = q[0], q[-1]
            if right in edges:
                neighbor = edges.pop(right)[0]
                self.remove_edge(edges, neighbor, right)
                q.append(neighbor)
            if left in edges:
                neighbor = edges.pop(left)[0]
                self.remove_edge(edges, neighbor, left)
                q.appendleft(neighbor)

        return list(q)
