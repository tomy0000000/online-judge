# Let n be the length of nums
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0

        if length == 2:
            return max(range(length), key=lambda x: nums[x])

        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
