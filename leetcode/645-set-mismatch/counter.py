# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nc = Counter(nums)
        oc = Counter(range(1, len(nums) + 1))
        return [list((nc - oc).keys())[0], list((oc - nc).keys())[0]]
