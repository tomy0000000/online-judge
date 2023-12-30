from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        return x**n
