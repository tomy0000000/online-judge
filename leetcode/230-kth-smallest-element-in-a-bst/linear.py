# Let n be the number of nodes in the tree.
#
# Time: O(n)
# Space: O(1)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        # Reaching smallest
        current = root
        while current.left:
            stack.append(current)
            current = current.left

        k -= 1
        while k > 0:
            right_nodes = self.nodes_count(current.right)
            if k > right_nodes:  # answer is in the left subtree or parent
                k -= right_nodes
            else:  # answer is in the right subtree
                return self.kthSmallest(current.right, k)
            if stack:  # If there is a parent
                current = stack.pop()
                k -= 1
                print(f"{current.val} {k} {[n.val for n in stack]}")
                if k == 0:
                    return current.val

        return current.val
