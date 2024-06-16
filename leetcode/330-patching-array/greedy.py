# Let n be the length of nums
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        miss = 1
        add = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                add += 1
        return add
