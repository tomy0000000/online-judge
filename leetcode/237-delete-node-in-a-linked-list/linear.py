# Let n be the length of the linked list
#
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        while node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
