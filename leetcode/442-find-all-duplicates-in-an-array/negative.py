# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        results = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                results.append(n)
            nums[n - 1] *= -1

        return results
