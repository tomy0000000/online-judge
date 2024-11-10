# Let n be the max depth of the tree
#
# Time: O(n)
# Space: O(n)

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def path_to_root(self, n: Node) -> list[Node]:
        path = [n]
        while n.parent is not None:
            path.append(n.parent)
            n = n.parent
        return path

    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        p_path = self.path_to_root(p)
        q_path = self.path_to_root(q)

        lca = p_path[-1]
        while p_path and q_path and p_path[-1].val == q_path[-1].val:
            lca = p_path.pop()
            q_path.pop()

        return lca
