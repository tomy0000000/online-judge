# Let n be the length nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter
from math import ceil


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans
