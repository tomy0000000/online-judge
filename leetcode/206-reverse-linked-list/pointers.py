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
        prev, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            # cur.next, cur, prev = prev, cur.next, cur
        return prev
