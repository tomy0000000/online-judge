# Let n be the length of all lists combined, and k be the number of lists.
#
# Time: O(nk)
# Space: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_min_list_index(self, lists: list[Optional[ListNode]]):
        heads = [(l.val, i) for i, l in enumerate(lists)]
        pick_i = min(heads)[1]
        return pick_i

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l is not None]
        if not lists:
            return None

        pick_i = self.find_min_list_index(lists)
        merged = lists[pick_i]

        next_node = lists[pick_i].next
        if next_node is None:
            lists.pop(pick_i)
        else:
            lists[pick_i] = next_node

        ptr = merged
        while lists:
            pick_i = self.find_min_list_index(lists)
            ptr.next = lists[pick_i]
            ptr = ptr.next

            next_node = lists[pick_i].next
            if next_node is None:
                lists.pop(pick_i)
            else:
                lists[pick_i] = next_node

        return merged
