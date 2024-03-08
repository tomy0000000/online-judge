# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freqs = list(Counter(nums).values())
        maxi = max(freqs)
        return freqs.count(maxi) * maxi
