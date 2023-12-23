# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        standard = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for rm, n in special.items():
            num += n * s.count(rm)
            s = s.replace(rm, "")
        for c in s:
            num += standard[c]
        return num
