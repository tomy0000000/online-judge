# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums_set = set(nums)
        maxi = 0
        for n in nums:
            if n > maxi and -n in nums_set:
                maxi = n
        return maxi if maxi > 0 else -1
