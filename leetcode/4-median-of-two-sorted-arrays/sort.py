# Let n be the length of nums1 and nums2 combined.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        tmp = nums1 + nums2
        tmp.sort()
        if len(tmp) % 2 == 0:
            return (tmp[len(tmp) // 2 - 1] + tmp[len(tmp) // 2]) / 2
        else:
            return tmp[(len(tmp) - 1) // 2]
