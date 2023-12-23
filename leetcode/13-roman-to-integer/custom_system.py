# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        standard = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        s = (
            s.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )
        for c in s:
            num += standard[c]
        return num
