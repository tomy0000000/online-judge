# Let n be the number of nodes in the tree.
#
# Time: O(n)
# Space: O(n)


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        if not root:
            return []
        children = []
        for n in root.children:
            children += self.postorder(n)
        return children + [root.val]
