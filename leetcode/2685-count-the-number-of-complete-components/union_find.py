# Let e be the number of edges and v be the number of nodes.
#
# Time: O(e + v)
# Space: O(e + v)

from collections import defaultdict


class Solution:
    def find_root(self, groups: dict, n: int):
        if groups[n] == n:
            return n
        root = self.find_root(groups, groups[n])
        groups[n] = root
        return root

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        roots = {}
        for a, b in edges:
            if a not in roots and b not in roots:
                roots[b] = a
                roots[a] = a
            elif a not in roots:
                roots[a] = self.find_root(roots, b)
            elif b not in roots:
                roots[b] = self.find_root(roots, a)
            else:
                roots[self.find_root(roots, b)] = self.find_root(roots, a)

        groups = defaultdict(set)
        for i in range(n):
            if i in roots:
                groups[self.find_root(roots, i)].add(i)
            else:
                groups[i].add(i)

        non = 0
        for _, group in groups.items():
            length = len(group)
            for m in group:
                if len(adj[m]) != length - 1:
                    non += 1
                    break

        return len(groups) - non
