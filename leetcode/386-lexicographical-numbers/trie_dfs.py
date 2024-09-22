# Time: O(n log n)
# Space: O(n)

from typing import Optional


# Definition for a trie node.
class TrieNode:
    def __init__(
        self, val: str, children: Optional[dict[int, Optional["TrieNode"]]] = None
    ):
        self.val = val
        self.children = children if children is not None else {}

    def insert(self, val: str) -> None:
        if not val:
            return

        first, rest = val[0], val[1:]
        if first not in self.children:
            self.children[first] = TrieNode(first)

        self.children[first].insert(rest)


class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, node: TrieNode, path: str):
        self.ans.append(int(path))
        for i in range(10):
            s = str(i)
            if s in node.children:
                self.dfs(node.children[s], f"{path}{s}")

    def lexicalOrder(self, n: int) -> list[int]:
        root = TrieNode("")
        for i in range(1, n + 1):
            root.insert(str(i))

        for i in range(10):
            s = str(i)
            if s in root.children:
                self.dfs(root.children[s], s)

        return self.ans
