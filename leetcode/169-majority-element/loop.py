# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = defaultdict(int)
        length = len(nums)
        for n in nums:
            c[n] += 1
            if c[n] > length / 2:
                return n
