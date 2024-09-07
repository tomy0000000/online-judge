from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_path(self, head, root):
        if not head:
            return True

        if not root or head.val != root.val:
            return False

        return self.check_path(head.next, root.left) or self.check_path(
            head.next, root.right
        )

    def isSubPath(
        self,
        head: Optional[ListNode],
        root: Optional[TreeNode],
    ) -> bool:
        if not root:
            return False

        if head.val == root.val and self.check_path(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
