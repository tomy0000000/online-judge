# Let n be the number of nodes in the graph
#
# Time: O(n)
# Space: O(1)
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def construct(self, new: Optional[Node], node: Optional[Node]):
        if new.val in self.constructed:
            return

        self.constructed[new.val] = True
        for nb in node.neighbors:
            if nb.val not in self.nodes:
                self.nodes[nb.val] = Node(nb.val)
            new_nb = self.nodes[nb.val]
            new.neighbors.append(new_nb)
            self.construct(new_nb, nb)

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        self.constructed = {}
        n = Node(node.val)
        self.nodes = {node.val: n}

        self.construct(n, node)
        return n
