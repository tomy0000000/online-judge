# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        return len(list(filter(lambda n: n % 2 == 0, nums))) > 1
