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
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        acc = {0: None}
        acc_rev = {None: 0}
        summ = 0
        while cur:
            summ += cur.val
            if summ in acc:
                prev = acc[summ]
                if prev is None:
                    rm = head
                    while rm != cur:
                        acc.pop(acc_rev[rm])
                        rm = rm.next
                    head = cur.next
                else:
                    rm = prev.next
                    while rm != cur:
                        acc.pop(acc_rev[rm])
                        rm = rm.next
                    prev.next = cur.next
            else:
                acc[summ] = cur
                acc_rev[cur] = summ
            cur = cur.next

        return head
