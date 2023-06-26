# Let n be the length of nums.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table: dict = {}
        for index, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], index]
            table[num] = index
        return []
