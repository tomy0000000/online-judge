# Let e be the number of edges and v be the number of nodes.
#
# Time: O(e + v)
# Space: O(e + v)

from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        print(adj)

        groups = defaultdict(set)
        component = 0
        visited = set()
        stack = []
        while len(visited) != n:
            print(f"new comp {visited=}")
            component += 1

            for i in range(n):
                print(f"{i=} {n=}, {visited}")
                if i not in visited:
                    stack = [i]
                    visited.add(i)
                    groups[component].add(i)
                    print(f"Visit {i}")
                    break
            else:
                assert False

            while stack:
                here = stack.pop()
                for i in adj[here]:
                    if i not in visited:
                        stack.append(i)
                    visited.add(i)
                    groups[component].add(i)
                    print(f"Visit {i}")

        non = 0
        for _, group in groups.items():
            length = len(group)
            for m in group:
                if len(adj[m]) != length - 1:
                    non += 1
                    break

        return component - non
