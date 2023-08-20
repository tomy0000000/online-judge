# Let n be the length of n
#
# Time: O(n)
# Space: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            if n % 2:
                bits += 1
            n >>= 1

        return bits
