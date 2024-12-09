# Let n be the length of nums, and m be the length of queries
#
# Time: O(n)
# Space: O(m log n)

from bisect import bisect_left


class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        same_par = []
        for i in range(len(nums) - 1):
            if (nums[i] + nums[i + 1]) % 2 == 0:
                same_par.append(i)

        ans = []
        for s, e in queries:
            left = bisect_left(same_par, s)
            right = bisect_left(same_par, e)
            ans.append(left == right)
        return ans
