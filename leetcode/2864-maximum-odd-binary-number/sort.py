# Let n be the length of s
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(sorted(s, reverse=True)[1:]) + "1"
