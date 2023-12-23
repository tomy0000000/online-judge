# Let n be the length of all lists combined, and k be the number of lists.
#
# Time: O(n^2)
# Space: O(1)

from bisect import insort
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l is not None]
        if not lists:
            return None

        lists.sort(key=lambda x: x.val, reverse=True)

        merged = lists[-1]

        next_node = lists[-1].next
        lists.pop()
        if next_node is not None:
            insort(lists, next_node, key=lambda x: -x.val)

        ptr = merged
        while lists:
            ptr.next = lists[-1]
            ptr = ptr.next

            next_node = lists[-1].next
            lists.pop()
            if next_node is not None:
                insort(lists, next_node, key=lambda x: -x.val)

        return merged
