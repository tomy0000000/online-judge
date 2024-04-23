# Let m be the length of edges.
#
# Time: O(m + n)
# Space: O(n)

from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        neighbor_map = {i: set() for i in range(n)}
        for node_1, node_2 in edges:
            neighbor_map[node_1].add(node_2)
            neighbor_map[node_2].add(node_1)

        leaves = deque(
            node for node, neighbors in neighbor_map.items() if len(neighbors) == 1
        )
        MARKER = -1
        leaves.append(MARKER)
        while len(neighbor_map) > 2 or (leaves[0] != MARKER and leaves[-1] != MARKER):
            leaf = leaves.popleft()
            if leaf == MARKER:
                leaves.append(MARKER)
                continue
            for neighbor in neighbor_map[leaf]:
                neighbor_map[neighbor].remove(leaf)
                if len(neighbor_map[neighbor]) == 1:
                    leaves.append(neighbor)
            neighbor_map.pop(leaf)

        return list(neighbor_map)
