# Let n be the length of the input list.
#
# Time: O(n)
# Space: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head.next
        batch_head = new_head
        ptr = batch_head.next
        while ptr:
            if ptr.val != 0:
                batch_head.val += ptr.val
                ptr = ptr.next
            else:
                batch_head.next = ptr.next
                batch_head = ptr.next
                ptr = batch_head.next if batch_head else None
        return new_head
