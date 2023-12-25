# Let n be the length of head.
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast, new_head, tail = head, head, None, None
        while fast:
            # Advance fast k steps
            for _ in range(k):
                if not fast:
                    return new_head
                fast = fast.next

            # Reverse from slow to fast
            prev_tail = tail
            prev, cur, tail = None, slow, slow
            while cur != fast:
                cur.next, cur, prev = prev, cur.next, cur

            # Connect the reversed part to the previous part and the next part
            if prev_tail:
                prev_tail.next = prev
            tail.next = fast

            # Advance slow and record the new head
            slow = fast
            new_head = new_head or prev  # only update on the first reversion
        return new_head
