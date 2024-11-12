# Let n be the number of nodes in the binary search tree
#
# Time: O(n)
# Space: O(n)

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root: Optional[Node]) -> None:
        if root is None:
            return

        self.traverse(root.left)
        self.in_order.append(root)
        self.traverse(root.right)

    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        self.in_order = []
        self.traverse(root)

        length = len(self.in_order)
        for i, node in enumerate(self.in_order):
            node.left = self.in_order[(i - 1) % length]
            node.right = self.in_order[(i + 1) % length]

        return self.in_order[0] if self.in_order else None
