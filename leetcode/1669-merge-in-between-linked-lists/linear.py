# Let n be the length of list1 and list2 combined
#
# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        left = list1
        for _ in range(a - 1):
            left = left.next

        right = left
        for _ in range(b - a + 2):
            right = right.next

        left.next = list2
        while left.next:
            left = left.next

        left.next = right

        return list1
