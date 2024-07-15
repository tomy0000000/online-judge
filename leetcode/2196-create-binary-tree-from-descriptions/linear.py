# Let n be the length of descriptions.
#
# Time: O(n)
# Space: O(n)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        mapping = {}
        roots = set()
        for p, c, left in descriptions:
            if p not in mapping:
                mapping[p] = TreeNode(val=p)
                roots.add(p)
            parent = mapping[p]

            if c not in mapping:
                mapping[c] = TreeNode(val=c)
            elif c in roots:
                roots.remove(c)
            child = mapping[c]

            if left:
                parent.left = child
            else:
                parent.right = child

        return mapping[next(iter(roots))]
