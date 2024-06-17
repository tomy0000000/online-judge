# Time: O(sqrt(n))
# Space: O(1)

from math import isqrt


class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        left, right = 0, isqrt(n)
        while left <= right:
            square_sum = left * left + right * right
            if square_sum == n:
                return True
            if square_sum < n:
                left += 1
            if square_sum > n:
                right -= 1
        return False
