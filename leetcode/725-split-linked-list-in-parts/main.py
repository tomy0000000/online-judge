# Let n be the number of nodes in the linked list.
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
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> list[Optional[ListNode]]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        odds = count % k
        each = (count - odds) // k

        ans = []
        current = head
        for part_index in range(k):
            if odds:
                part_num = each + 1
                odds -= 1
            else:
                part_num = each

            if current:
                ans.append(current)
                part_num -= 1
                while part_num:
                    current = current.next
                    part_num -= 1
                end = current
                if current:
                    current = current.next
                    end.next = None
            else:
                ans.append(None)

        return ans
