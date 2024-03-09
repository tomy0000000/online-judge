# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1, p2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        while p1 != l1 and p2 != l2:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return -1
