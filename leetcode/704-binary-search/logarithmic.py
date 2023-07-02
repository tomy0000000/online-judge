# Let n be the length of nums
#
# Time: O(log(n))
# Space: O(1)


class Solution:
    def binary_search(self, nums: list[int], target: int, begin: int, end: int) -> int:
        if end - begin <= 3:
            for i in range(begin, end + 1):
                if nums[i] == target:
                    return i
            return -1

        mid_index = (begin + end) // 2
        mid = nums[mid_index]
        if mid == target:
            return mid_index
        if mid < target:
            return self.binary_search(nums, target, mid_index, end)
        if target < mid:
            return self.binary_search(nums, target, begin, mid_index)

    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
