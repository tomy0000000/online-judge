# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)

        return s.pop()
