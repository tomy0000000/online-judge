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

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        left = f"{left}L" if left else ""
        right = f"{right}R" if right else ""

        return f"{left}{root.val}V{right}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        stacks = {"left": [], "main": []}
        i = 0
        while i < len(data):
            if data[i] == "L":
                stacks["left"].append(stacks["main"].pop())
                i += 1
            elif data[i] == "R":
                right = stacks["main"].pop()
                parent = stacks["main"][-1]
                parent.right = right
                i += 1
            else:
                stop = data.find("V", i)
                n = TreeNode(int(data[i:stop]))
                if stacks["left"]:
                    n.left = stacks["left"].pop()
                stacks["main"].append(n)
                i = stop + 1
        return stacks["main"][0] if stacks["main"] else None
