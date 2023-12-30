import base64
import pickle
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        return base64.b64encode(pickle.dumps(root)).decode()

    def deserialize(self, data: str) -> Optional[TreeNode]:
        return pickle.loads(base64.b64decode(str.encode(data)))
