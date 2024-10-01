# Let n be the length of arr
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        c = Counter(n % k for n in arr)
        if c[0] % 2 != 0:
            return False
        for i in range(1, k):
            if c[i] != c[k - i]:
                return False
        return True
