# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findMissingRanges(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        if not nums:
            return [[lower, upper]]

        if len(nums) == 1:
            if lower == nums[0] == upper:
                return []

            if nums[0] < lower or upper < nums[0]:
                return [[lower, upper]]

            if nums[0] == lower:
                return [[lower + 1, upper]]

            if nums[0] == upper:
                return [[lower, upper - 1]]

            return [[lower, nums[0] - 1], [nums[0] + 1, upper]]

        ranges = []

        if lower < nums[0]:
            ranges.append([lower, nums[0] - 1])

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                ranges.append([nums[i] + 1, nums[i + 1] - 1])

        if nums[-1] < upper:
            ranges.append([nums[-1] + 1, upper])

        return ranges
