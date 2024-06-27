# Let n be the length of edges
#
# Time: O(1)
# Space: O(1)


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        nodes = set()
        for edge in edges:
            for n in edge:
                if n in nodes:
                    return n
                nodes.add(n)
