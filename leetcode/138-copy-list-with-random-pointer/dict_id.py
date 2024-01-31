# Let n be the length of the input list
#
# Time: O(n)
# Space: O(1)

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def request_node(self, old_node: Optional[Node]) -> Optional[Node]:
        if not old_node:
            return None

        key = hash(old_node)  # or id(old_node)
        if key in self.index:
            return self.index[key]

        self.index[key] = Node(old_node.val)
        return self.index[key]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        self.index = {}
        new_head = self.request_node(head)
        new_head.random = self.request_node(head.random)

        ptr_ref, ptr_new = head, new_head
        while ptr_ref.next:
            ptr_new.next = self.request_node(ptr_ref.next)
            ptr_new.next.random = self.request_node(ptr_ref.next.random)
            ptr_ref, ptr_new = ptr_ref.next, ptr_new.next

        return new_head
