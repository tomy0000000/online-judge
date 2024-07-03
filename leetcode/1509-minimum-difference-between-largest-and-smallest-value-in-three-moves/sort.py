# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)

from itertools import pairwise


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 4:
            return 0

        nums.sort()
        diff = [y - x for x, y in pairwise(nums)]

        if length == 5:
            return min(diff)

        maxi = 0
        ind = 0
        for i in range(4):
            left = diff[:i]
            right = diff[length - 4 + i :]
            summ = sum(left + right)
            if summ > maxi:
                maxi = summ
                ind = i

        return nums[ind - 4] - nums[ind]
