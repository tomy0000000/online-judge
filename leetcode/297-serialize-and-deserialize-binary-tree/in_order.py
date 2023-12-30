# Let n be the number of nodes in the tree.
#
# Time: O(n)
# Space: O(n)


from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        return self.deserialize_list(data.split(","))

    def deserialize_list(self, nums: list[str]) -> Optional[TreeNode]:
        val = nums.pop(0)
        if not val:
            return None

        root = TreeNode(val)
        root.left = self.deserialize_list(nums)
        root.right = self.deserialize_list(nums)

        return root
