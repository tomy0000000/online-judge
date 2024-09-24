# Let n be the length of arr1 + arr2
#
# Time: O(n)
# Space: O(n)


class Solution:
    def trie_put(self, trie: dict[int, dict], val: str) -> None:
        if not val:
            return

        c = val[0]
        if c not in trie:
            trie[c] = {}

        self.trie_put(trie[c], val[1:])

    def tries_common(self, t1: dict[int, dict], t2: dict[int, dict]) -> int:
        max_depth = 0
        for i in range(10):
            key = str(i)
            if key not in t1 or key not in t2:
                continue
            max_depth = max(max_depth, 1 + self.tries_common(t1[key], t2[key]))
        return max_depth

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        t1, t2 = {}, {}
        for n in arr1:
            self.trie_put(t1, str(n))
        for n in arr2:
            self.trie_put(t2, str(n))

        return self.tries_common(t1, t2)
