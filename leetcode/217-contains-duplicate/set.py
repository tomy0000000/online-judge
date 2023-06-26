# Let n be the length of nums.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
