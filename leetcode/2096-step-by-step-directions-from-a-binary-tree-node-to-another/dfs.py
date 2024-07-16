# Let n be the number of nodes in the binary tree.
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
    def __init__(self) -> None:
        self.startValue = None
        self.destValue = None
        self.startPath = None
        self.destPath = None
        self.abort = None

    def dfs(self, root: Optional[TreeNode], path: list[str]):
        if not root or self.abort:
            return

        if root.val == self.startValue:
            self.startPath = path.copy()

        if root.val == self.destValue:
            self.destPath = path.copy()

        if self.startPath is not None and self.destPath is not None:
            self.abort = True
            return

        if root.left:
            path.append("L")
            self.dfs(root.left, path)
            path.pop()

        if root.right:
            path.append("R")
            self.dfs(root.right, path)
            path.pop()

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        self.startValue = startValue
        self.destValue = destValue
        self.dfs(root, [])
        while (
            self.startPath and self.destPath and self.startPath[0] == self.destPath[0]
        ):
            self.startPath.pop(0)
            self.destPath.pop(0)

        return "U" * len(self.startPath) + "".join(self.destPath)
