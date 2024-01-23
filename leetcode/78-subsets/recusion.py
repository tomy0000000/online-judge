# Let n be the length of nums
#
# Time: O(n * 2^n)
# Space: O(n * 2^n)


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return [[]] + [
            [nums[i]] + sub
            for i in range(len(nums))
            for sub in self.subsets(nums[i + 1 :])
        ]
