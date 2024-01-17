# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(1)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left = self.sortColors(nums[:middle])
        right = self.sortColors(nums[middle:])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums
