# Let n be the length of head.
#
# Time: O(n)
# Space: O(1)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        previous = None
        while current:
            previous = ListNode(current.val, previous)
            current = current.next

        return previous
