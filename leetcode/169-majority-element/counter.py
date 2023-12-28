# Let n be the length of nums, and let m be the number of unique elements in nums
#
# Time: O(n)
# Space: O(m)

from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = Counter(nums)
        return max(c, key=lambda k: c[k])
