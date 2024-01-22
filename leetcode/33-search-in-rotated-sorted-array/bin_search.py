# Let n be the length of nums
#
# Time: O(log(n))
# Space: O(1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return -1 if nums[left] != target else left
