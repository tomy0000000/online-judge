# Let n be the length of the linked list.
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Only one node
        if not head.next:
            return head

        # Calculate length
        cur, length = head, 1
        while cur.next:
            cur = cur.next
            length += 1

        # Odd number of node and k is the middle node
        if 2 * k - 1 == length:
            return head

        # Node 1-index, where i < j
        i, j = k - 1, length - k
        if i > j:
            i, j = j, i

        # Find previous nodes of target nodes
        i_prev = j_prev = head
        for _ in range(i - 1):
            i_prev = i_prev.next
        for _ in range(j - 1):
            j_prev = j_prev.next
        print(f"{i=} {j=} {i_prev.val=} {j_prev.val=}")

        # Swap for different cases
        if length == 2:
            # The only two nodes
            print("The only two nodes")
            head.next.next, head.next, head = head, head.next.next, head.next
        elif i_prev.next == j_prev:
            # The two middle nodes
            print("The two middle nodes")
            j_prev.next.next, j_prev.next, i_prev.next = (
                i_prev.next,
                j_prev.next.next,
                j_prev.next,
            )
        elif k == 1 or k == length:
            # The head and tail nodes
            print("The head and tail nodes")
            head.next, head, j_prev.next.next, j_prev.next = (
                j_prev.next.next,
                j_prev.next,
                head.next,
                head,
            )
        else:
            # Other cases
            print("Other cases")
            i_prev.next.next, j_prev.next.next, i_prev.next, j_prev.next = (
                j_prev.next.next,
                i_prev.next.next,
                j_prev.next,
                i_prev.next,
            )

        return head
