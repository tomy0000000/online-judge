# Time: O(log n)
# Space: O(1)


from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        if x == 0:
            return 0
        if n == 0:
            return 1

        if n % 2 == 0:
            sqrt = self.myPow(x, n // 2)
            return sqrt * sqrt
        else:
            sqrt = self.myPow(x, (n - 1) // 2)
            return sqrt * sqrt * x
