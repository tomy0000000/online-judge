# Let n be the number of nodes in the tree
#
# Time: O(n)
# Space: O(n)

from collections import Counter, defaultdict, deque
from typing import Optional
from uuid import uuid4


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, None)])
        while queue:
            values = Counter()
            groups = defaultdict(set)

            for _ in range(len(queue)):
                node, parent = queue.popleft()
                values[parent] += node.val
                groups[parent].add(node)
                parent_id = uuid4()
                if node.left:
                    queue.append((node.left, parent_id))
                if node.right:
                    queue.append((node.right, parent_id))

            for parent, group in groups.items():
                new_val = values.total() - values[parent]
                for node in group:
                    node.val = new_val

        return root
