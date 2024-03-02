# Let n be the length of num
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(map(lambda x: x**2, nums))
