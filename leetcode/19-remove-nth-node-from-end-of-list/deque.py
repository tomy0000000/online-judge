# Let m be the length of the linked list.
#
# Time: O(m)
# Space: O(n)


from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        d = deque(maxlen=n + 1)
        length = 0
        while ptr:
            d.append(ptr)
            ptr = ptr.next
            length += 1

        if length == n:
            return head.next

        prev = d.popleft()
        prev.next = prev.next.next if prev.next else None

        return head
