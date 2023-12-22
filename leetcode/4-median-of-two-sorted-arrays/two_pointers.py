# Let n be the length of nums1 and nums2 combined.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        length_one, length_two = len(nums1), len(nums2)
        length = length_one + length_two
        even = bool(length % 2 == 0)

        if not nums1 or not nums2:
            the_list = nums1 or nums2
            if even:
                return (the_list[length // 2 - 1] + the_list[length // 2]) / 2
            else:
                return the_list[(length - 1) // 2]

        med_index = length // 2 + 1 if even else (length + 1) // 2
        ptr1, ptr2 = -1, -1
        last_meds = []
        while med_index:
            med_index -= 1

            one = False
            if ptr1 == length_one - 1:
                one = False
            elif ptr2 == length_two - 1:
                one = True
            elif nums1[ptr1 + 1] < nums2[ptr2 + 1]:
                one = True

            if one:
                ptr1 += 1
                if med_index <= 1:
                    last_meds.append(nums1[ptr1])
            else:
                ptr2 += 1
                if med_index <= 1:
                    last_meds.append(nums2[ptr2])

        if even:
            return (last_meds[0] + last_meds[1]) / 2
        else:
            return last_meds[-1]
