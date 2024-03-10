# Let n be the length of nums1 and nums2
#
# Time: O(n)
# Space: O(n)


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))
