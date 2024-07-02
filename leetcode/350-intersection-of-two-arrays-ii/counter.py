# Let n be the length of nums1 + length of nums2
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ca = {n: min(c1[n], c2[n]) for n in set(c1 + c2)}
        return [n for n, count in ca.items() for _ in range(count)]
