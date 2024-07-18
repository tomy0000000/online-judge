# Let n be the number of nodes in the tree.
#
# Time: O(n log n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.leaves = set()
        self.parents = {}

    def dfs(self, root: TreeNode) -> None:
        if not root:
            return

        if not root.left and not root.right:
            self.leaves.add(root)
            return

        if root.left:
            self.parents[root.left] = root
            self.dfs(root.left)

        if root.right:
            self.parents[root.right] = root
            self.dfs(root.right)

    def neighbors(self, root: TreeNode) -> list[TreeNode]:
        neighbors = []
        if root in self.parents:
            neighbors.append(self.parents[root])
        if root.left:
            neighbors.append(root.left)
        if root.right:
            neighbors.append(root.right)
        return neighbors

    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root.left and not root.right:
            return 0

        self.dfs(root)

        good = 0
        for leaf in self.leaves:
            visited = {leaf}
            stack = [(self.parents[leaf], distance - 1)]
            while stack:
                node, dist = stack.pop()
                visited.add(node)
                if node in self.leaves:
                    good += 1
                    continue

                if dist == 0:
                    continue

                for neighbor in self.neighbors(node):
                    if neighbor in visited:
                        continue
                    stack.append((neighbor, dist - 1))

        return good // 2
