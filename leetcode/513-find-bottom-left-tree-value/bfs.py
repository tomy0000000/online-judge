# Let n be the number of nodes in the tree
#
# Time: O(n)
# Space: O(n)


from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val

        queue = deque([root])
        while queue:
            level_queue = deque()
            last_level = True
            while queue:
                node = queue.popleft()
                for child in (node.left, node.right):
                    if not child:
                        continue
                    level_queue.append(child)
                    if child.left or child.right:
                        last_level = False
            if last_level:
                return level_queue.popleft().val
            queue = level_queue
