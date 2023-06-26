# Let n be the length of nums.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mapping = {}
        for n in nums:
            if n in mapping:
                return True
            mapping[n] = True
        return False
