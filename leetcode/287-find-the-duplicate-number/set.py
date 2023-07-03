# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return n
            else:
                nums_set.add(n)
