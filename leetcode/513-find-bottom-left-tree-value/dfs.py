# Let n be the number of nodes in the tree
#
# Time: O(n)
# Space: O(n)

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

        stack = [(root, 0)]
        maxi, maxi_depth = root.val, 0
        while stack:
            node, depth = stack.pop()
            if depth > maxi_depth:
                maxi = node.val
                maxi_depth = depth
            for child in (node.right, node.left):
                if not child:
                    continue
                stack.append((child, depth + 1))
        return maxi
