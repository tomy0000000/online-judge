from math import isqrt


class Solution:
    def is_perfect_square(self, n: int) -> bool:
        return n == isqrt(n) ** 2

    def is_two_perfect_square_sum(self, n: int) -> bool:
        # Use two pointers to check if n can be represented as the sum of two squares
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

    def legendre_three_square(self, n: int) -> bool:
        # remove all factors of 4
        while n % 4 == 0:
            n //= 4

        # if n is of the form 8b + 7
        if n % 8 == 7:
            return False

        return True

    def numSquares(self, n: int) -> int:
        if self.is_perfect_square(n):
            return 1

        if self.is_two_perfect_square_sum(n):
            return 2

        # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
        #
        # n can be represented as the sum of three squares
        # iff n does not have the form
        #
        # n = 4^a * (8b + 7)
        if self.legendre_three_square(n):
            return 3

        # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
        # All positive integers can be expressed as the sum of four integer squares
        return 4
