# Let n be the number of nodes in the graph
#
# Time: O(n)
# Space: O(1)
from copy import deepcopy
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        return deepcopy(node)
