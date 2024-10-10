# Let n be the length of the linked list
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next

        prev = None
        left = head
        while left and left.next:
            right = left.next
            if prev:
                prev.next, left.next, right.next = right, right.next, left
            else:
                left.next, right.next = right.next, left
            prev, left = left, left.next

        return new_head
