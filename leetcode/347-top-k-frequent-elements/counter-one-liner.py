# Let n be the length of nums, and m be the number of unique numbers in nums.
#
# Time: O(n + m log m)
# Space: O(m)

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
