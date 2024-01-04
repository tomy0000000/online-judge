# Let n be the length of the linked list
#
# Time: O(n)
# Space: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                return True
        return False
