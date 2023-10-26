# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        rest = n
        num_of_threes = 0
        while rest > 4:
            rest -= 3
            num_of_threes += 1

        return 3**num_of_threes * rest
