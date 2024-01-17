# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(1)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        nums.sort()
