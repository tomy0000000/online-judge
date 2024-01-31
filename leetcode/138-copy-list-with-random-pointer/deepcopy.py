# Let n be the length of the input list
#
# Time: O(n)
# Space: O(1)

from copy import deepcopy
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        return deepcopy(head)
