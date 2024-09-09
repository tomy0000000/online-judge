# Let k be the length of the linked list.
#
# Time: O(k)
# Space: O(m * n)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        xx, yy = m - 1, n - 1
        x, y, face, face_limit = 0, 0, 0, n
        mat = [[-1 for _ in range(n)] for _ in range(m)]
        ptr = head
        while ptr:
            mat[x][y] = ptr.val
            ptr = ptr.next
            face_limit -= 1
            if face_limit == 0:
                face = 0 if face == 3 else face + 1
                if face % 2 == 0:
                    face_limit = yy
                    yy -= 1
                else:
                    face_limit = xx
                    xx -= 1
            if face == 0:
                y += 1
            elif face == 1:
                x += 1
            elif face == 2:
                y -= 1
            else:
                x -= 1
        return mat
