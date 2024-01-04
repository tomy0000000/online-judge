# Let n be the length nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            if c % 2 != 0:
                c -= 3
                ans += 1
            ans += c // 6 * 2  # 2 ops per 6 numbers
            ans += c % 6 // 2  # 0 -> 0, 2 -> 1, 4 -> 2
        return ans
