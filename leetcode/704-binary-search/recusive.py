# Let n be the length of nums
#
# Time: O(log(n))
# Space: O(1)


class Solution:
    def binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        if right < left:
            return -1

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, right)
        else:
            return self.binary_search(nums, target, left, mid - 1)

    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
