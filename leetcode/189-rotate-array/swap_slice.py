# Let n be the length of the input list
#
# Time: O(n)
# Space: O(1)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) == 1 or k == 0 or len(nums) == k:
            return
        k %= len(nums)
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
