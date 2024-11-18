# Let n be the length of the linked list
#
# Time: O(n * log(n))
# Space: O(1)

from heapq import heappop, heappush
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        ptr = head
        heap = []
        while ptr:
            heappush(heap, ptr.val)
            ptr = ptr.next

        ptr = head
        while ptr:
            ptr.val = heappop(heap)
            ptr = ptr.next

        return head
