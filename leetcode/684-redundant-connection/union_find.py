# Let n be the number of nodes
#
# Time: O(n)
# Space: O(n)


class Solution:
    def find_root(self, nodes, n):
        if nodes[n] == -1:
            return n

        return self.find_root(nodes, nodes[n])

    def add_edge(self, nodes, a, b) -> bool:
        if a in nodes and b in nodes:
            root_a = self.find_root(nodes, a)
            root_b = self.find_root(nodes, b)
            if root_a == root_b:
                return True

            nodes[root_b] = root_a
            return False

        if a not in nodes and b not in nodes:
            nodes[a] = -1
            nodes[b] = a
            return False

        if a in nodes:
            root_a = self.find_root(nodes, a)
            nodes[b] = root_a
        else:
            root_b = self.find_root(nodes, b)
            nodes[a] = root_b
        return False

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        nodes = {}
        for a, b in edges:
            if self.add_edge(nodes, a, b):
                break
        return [a, b]
