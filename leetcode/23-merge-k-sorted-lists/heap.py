# Let n be the length of all lists combined, and k be the number of lists.
#
# Time: O(n log n)
# Space: O(1)

from heapq import heapify, heappop, heappush
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_min_node(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        node = heappop(lists)[1]
        next_node = node.next
        if next_node is not None:
            heappush(lists, (next_node.val, next_node))
        return node

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        lists = [(l.val, l) for l in lists if l is not None]
        if not lists:
            return None

        heapify(lists)

        merged = self.get_min_node(lists)
        ptr = merged

        while lists:
            ptr.next = self.get_min_node(lists)
            ptr = ptr.next

        return merged
