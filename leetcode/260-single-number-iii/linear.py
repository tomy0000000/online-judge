# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        if len(nums) == 2:
            return nums

        xor = reduce(lambda a, b: a ^ b, nums)
        set_bit = xor & -xor

        arr_1 = []
        arr_2 = []
        for n in nums:
            if n & set_bit == 0:
                arr_1.append(n)
            else:
                arr_2.append(n)

        return [reduce(lambda a, b: a ^ b, arr_1), reduce(lambda a, b: a ^ b, arr_2)]
