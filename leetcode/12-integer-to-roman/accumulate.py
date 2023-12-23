# Let n be the number of digits in num.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        roman = ""
        for n, c in num_map.items():
            while n <= num:
                roman += c
                num -= n
            if num == 0:
                break
        return roman
