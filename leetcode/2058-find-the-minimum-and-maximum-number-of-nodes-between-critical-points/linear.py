# Let n be the length of the linked list.
#
# Time: O(n)
# Space: O(1)

from itertools import pairwise
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        criticals = []
        one, two, three = head, head.next, head.next.next
        ind = 1
        while three:
            if one.val < two.val and two.val > three.val:
                criticals.append(ind)
            elif one.val > two.val and two.val < three.val:
                criticals.append(ind)
            one, two, three = one.next, two.next, three.next
            ind += 1
        if len(criticals) < 2:
            return [-1, -1]
        diffs = [y - x for x, y in pairwise(criticals)]
        return [min(diffs), criticals[-1] - criticals[0]]
