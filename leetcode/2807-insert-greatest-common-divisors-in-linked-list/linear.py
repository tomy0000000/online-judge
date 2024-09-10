from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev, ptr = head, head.next
        while ptr:
            new_val = gcd(prev.val, ptr.val)
            prev.next = ListNode(new_val, ptr)
            prev, ptr = ptr, ptr.next
        return head
