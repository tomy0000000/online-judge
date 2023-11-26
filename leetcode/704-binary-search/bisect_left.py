# Let n be the length of nums
#
# Time: O(log(n))
# Space: O(1)


from bisect import bisect_left


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        index = bisect_left(nums, target)
        return index if index != len(nums) and nums[index] == target else -1
