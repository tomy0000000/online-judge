# Let n be the length of s
#
# Time: O(n log n)
# Space: O(n)


from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = defaultdict(lambda: 27)
        for i, c in enumerate(order):
            rank[c] = i

        return "".join(sorted(list(s), key=lambda c: rank[c]))
