# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        standard = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i, c in enumerate(s):
            num += standard[c]
            if i == 0:
                continue
            if c in "VX" and s[i - 1] == "I":
                num -= 2
            if c in "LC" and s[i - 1] == "X":
                num -= 20
            if c in "DM" and s[i - 1] == "C":
                num -= 200
        return num
