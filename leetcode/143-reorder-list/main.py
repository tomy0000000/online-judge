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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return

        # Count length
        count = 1
        current = head
        while current.next:
            current = current.next
            count += 1

        # Find mid
        mid = count // 2 + 1
        current = head
        while mid:
            if mid == 1:
                last = current
            current = current.next
            mid -= 1
        last.next = None

        # Push into stack
        stack = current
        stack_next = stack.next
        current.next = None
        while stack_next:
            old_stack = stack
            stack = stack_next
            org_next = stack_next.next
            stack.next = old_stack
            stack_next = org_next

        # Merge
        current = head
        while stack:
            cur_next = current.next
            stack_next = stack.next
            current.next = stack
            stack.next = cur_next
            current = cur_next
            stack = stack_next
