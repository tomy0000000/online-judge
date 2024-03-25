# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        return [n for n, c in Counter(nums).items() if c == 2]
