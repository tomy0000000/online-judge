# Let n be the length of the linked list
#
# Time: O(n)
# Space: O(n)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head:
            i = id(head)
            if i in nodes:
                return True
            nodes.add(i)
            head = head.next
        return False
