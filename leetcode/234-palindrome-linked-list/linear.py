# Let n be the length of the linked list
#
# Time: O(n)
# Space: O(n)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = [head.val]
        cur = head
        while cur.next:
            cur = cur.next
            nums.append(cur.val)
        return nums == nums[::-1]
