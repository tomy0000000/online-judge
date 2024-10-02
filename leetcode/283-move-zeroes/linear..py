# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        indexes = []
        for i, n in enumerate(nums):
            if n == 0:
                indexes.append(i)

        for i in reversed(indexes):
            nums.append(nums.pop(i))
