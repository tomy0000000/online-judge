# Let n be the number of nodes in the tree.
#
# Time: O(n)
# Space: O(n)

from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    edges: dict[int, set[int]]

    def build_graph(
        self, root: Optional[TreeNode], parent: Optional[int] = None
    ) -> None:
        if not root:
            return

        val = root.val
        if parent:
            self.edges[val].add(parent)
        if root.left:
            self.edges[val].add(root.left.val)
            self.build_graph(root.left, val)
        if root.right:
            self.edges[val].add(root.right.val)
            self.build_graph(root.right, val)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.edges = defaultdict(set)
        self.build_graph(root)

        queue = deque([(start, 0)])
        visited = {start}
        dist = 0
        while queue:
            n, dist = queue.popleft()
            for i in self.edges[n]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, dist + 1))

        return dist
