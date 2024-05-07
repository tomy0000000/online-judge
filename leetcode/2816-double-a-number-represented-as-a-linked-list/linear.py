# Let n be the length of the linked list
#
# Time: O(n)
# Space: O(1)

import sys
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        sys.set_int_max_str_digits(0)

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        digits = []
        ptr = head
        nodes = []
        while ptr:
            nodes.append(ptr)
            digits.append(str(ptr.val))
            ptr = ptr.next

        num = int("".join(digits)) * 2
        digits = list(str(num))

        new_nodes = len(digits) - len(nodes)
        for _ in range(new_nodes):
            node = ListNode()
            nodes[-1].next = node
            nodes.append(node)

        for i, n in enumerate(nodes):
            n.val = digits[i]

        return head
