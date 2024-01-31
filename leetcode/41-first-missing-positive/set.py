# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        missing = set(range(1, len(nums) + 1))
        for n in nums:
            missing.discard(n)
        return min(missing) if missing else len(nums) + 1
