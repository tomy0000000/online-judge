# Let n be the number of digits in num.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def digit_to_roman(self, digit: str, pos: int) -> str:
        mapping = {
            "0": "",
            "1": "0",
            "2": "00",
            "3": "000",
            "4": "01",
            "5": "1",
            "6": "10",
            "7": "100",
            "8": "1000",
            "9": "02",
        }
        chars = ["IVX", "XLC", "CDM", "M--"]
        table = str.maketrans("012", chars[pos])
        return mapping[digit].translate(table)

    def intToRoman(self, num: int) -> str:
        romans = []
        for pos, digit in enumerate(str(num)[::-1]):
            digit_roman = self.digit_to_roman(digit, pos)
            romans.append(digit_roman)
        return "".join(romans[::-1])
