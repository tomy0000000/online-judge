# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from math import inf


class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        cur_set = bin(nums[0])[2:].count("1")
        group_min, group_max = inf, 0
        prev_max = 0
        for n in nums:
            set_count = bin(n)[2:].count("1")
            if set_count != cur_set:
                if group_min < prev_max:
                    return False
                prev_max = group_max
                cur_set = set_count
                group_min, group_max = n, n
            else:
                group_max = max(group_max, n)
                group_min = min(group_min, n)

        if group_min < prev_max:
            return False

        return True
