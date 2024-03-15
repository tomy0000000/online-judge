# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from functools import reduce


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if nums.count(0) >= 2:
            return [0] * len(nums)

        product = reduce(lambda a, b: a * b, nums)
        zero_product = reduce(lambda a, b: a * b, filter(lambda x: x != 0, nums))

        return [product // n if n != 0 else zero_product for n in nums]
