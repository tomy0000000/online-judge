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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head
        while ptr:
            while stack and ptr.val > stack[-1].val:
                stack.pop()
            stack.append(ptr)
            ptr = ptr.next

        for i, n in enumerate(stack):
            if i + 1 == len(stack):
                n.next = None
            else:
                n.next = stack[i + 1]

        return stack[0]
