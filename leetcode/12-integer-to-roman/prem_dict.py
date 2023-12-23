# Let n be the number of digits in num.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def intToRoman(self, num: int) -> str:
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
        chars_for_pos = ["IVX", "XLC", "CDM", "M"]
        roman = ""
        for pos, digit in enumerate(str(num)[::-1]):
            perm = mapping[digit]
            chars = chars_for_pos[pos]
            digit_roman = ""
            for c in perm:
                digit_roman += chars[int(c)]
            roman = digit_roman + roman
        return roman
