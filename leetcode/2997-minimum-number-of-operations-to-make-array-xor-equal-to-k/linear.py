# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from functools import reduce


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        target_bin = bin(k)[2:]

        existed = reduce(lambda a, b: a ^ b, nums)
        existed_bin = bin(existed)[2:]

        length = max(len(target_bin), len(existed_bin))
        target_bin = f"{target_bin:0>{length}}"
        existed_bin = f"{existed_bin:0>{length}}"

        diffs = sum(1 for b1, b2 in zip(target_bin, existed_bin) if b1 != b2)

        return diffs
