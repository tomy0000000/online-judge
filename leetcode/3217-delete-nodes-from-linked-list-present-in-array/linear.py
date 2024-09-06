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
    def modifiedList(
        self, nums: list[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        num_set = set(nums)

        while head.val in num_set:
            head = head.next

        ptr = head
        while ptr.next:
            if ptr.next.val in num_set:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next

        return head
