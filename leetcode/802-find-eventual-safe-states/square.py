# Let n be the node number of graph.
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # Find terminal nodes
        safe = set()
        for node, paths in enumerate(graph):
            if not paths:
                safe.add(node)

        # Update safe until stable
        changed = True
        while changed:
            changed = False
            for node, paths in enumerate(graph):
                if node not in safe and all([(p in safe) for p in paths]):
                    safe.add(node)
                    changed = True

        ans = list(safe)
        ans.sort()
        return ans
