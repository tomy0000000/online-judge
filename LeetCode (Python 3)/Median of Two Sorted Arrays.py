class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tmp = nums1 + nums2
        tmp.sort()
        if len(tmp)%2 == 0:
            # print(tmp[len(tmp)//2 - 1] + tmp[len(tmp)//2] / 2)
            return (tmp[len(tmp)//2 - 1] + tmp[len(tmp)//2]) / 2
        else:
            # print(tmp[(len(tmp)-1) // 2])
            return tmp[(len(tmp)-1) // 2]
