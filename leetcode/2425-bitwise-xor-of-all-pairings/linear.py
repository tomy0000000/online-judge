# Let n be the length of nums1 and m be the length of nums2
#
# Time: O(n + m)
# Space: O(1)

from functools import reduce


class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        def xor(x, y):
            return x ^ y

        n1, n2 = len(nums1), len(nums2)
        left = reduce(xor, nums1) if n2 % 2 == 1 else 0
        right = reduce(xor, nums2) if n1 % 2 == 1 else 0
        return left ^ right
