# Let n, m be the length of list1 and list2 respectively.
#
# Time: O(n + m)
# Space: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        current = None
        while list1 or list2:
            if not list2 or (list1 and list2 and list1.val < list2.val):
                node = list1
                list1 = list1.next
                node.next = None
                if not current:
                    current = node
                    head = current
                else:
                    current.next = node
                    current = current.next
            else:
                node = list2
                list2 = list2.next
                node.next = None
                if not current:
                    current = node
                    head = current
                else:
                    current.next = node
                    current = current.next
        return head
