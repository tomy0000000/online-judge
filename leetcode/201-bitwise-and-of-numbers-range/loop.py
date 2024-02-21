# Time: O(1)
# Space: O(1)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return left & right
