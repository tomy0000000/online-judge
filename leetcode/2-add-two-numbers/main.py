# Let m, n be the length of l1 and l2.
#
# Time: O(m + n)
# Space: O(m + n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def readNode(self, n: Optional[ListNode]):
        tmp = [n.val]
        while n.next:
            n = n.next
            tmp.append(n.val)
        return tmp[::-1]

    def rebuildNode(self, node_list: list[str]):
        last = None
        for each in node_list:
            tmp = ListNode(each)
            if last:
                tmp.next = last
            last = tmp
        return last

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = int("".join([str(x) for x in self.readNode(l1)]))
        num2 = int("".join([str(x) for x in self.readNode(l2)]))
        return self.rebuildNode(list(str(num1 + num2)))
