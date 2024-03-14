# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        one_indexes = [i for i, n in enumerate(nums) if n == 1]
        one_indexes = [-1] + one_indexes + [len(nums)]
        comb = 0
        for left in range(1, len(one_indexes) - goal):
            if goal == 0:
                length = one_indexes[left] - one_indexes[left - 1] - 1
                new_comb = (1 + length) * length // 2
            else:
                right = left + goal - 1
                z_left = one_indexes[left] - one_indexes[left - 1] - 1
                z_right = one_indexes[right + 1] - one_indexes[right] - 1
                new_comb = (z_left + 1) * (z_right + 1)
            comb += new_comb
        return comb
