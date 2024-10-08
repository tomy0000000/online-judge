# Time: O(m + n)
# Space: O(1)


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        for i in range(m + n - 1, n - 1, -1):
            nums1[i - n], nums1[i] = nums1[i], nums1[i - n]

        p1, p2 = n, 0
        for i in range(m + n):
            if p1 >= m + n:
                nums1[i] = nums2[p2]
                p2 += 1
                continue

            if p2 >= n:
                nums1[i] = nums1[p1]
                p1 += 1
                continue

            if p1 < m + n and nums1[p1] <= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
