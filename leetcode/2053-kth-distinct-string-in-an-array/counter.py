# Let n be the length of arr
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counter = Counter(arr)
        distinct = set(c for c, n in counter.items() if n == 1)
        for c in arr:
            if c in distinct:
                k -= 1
            if not k:
                return c
        return ""
