# Time: O(n)
# Space: O(1)


class Solution:
    def numberToWords(self, num: int) -> str:
        words = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        if num in words:
            return words[num]

        billions = int(str(num // 1000000000)[-3:])
        millions = int(str(num // 1000000)[-3:])
        thousands = int(str(num // 1000)[-3:])
        hundreds = int(str(num // 100)[-1:])
        tenth_plus_digit = num % 100
        tenth = int(str(num // 10)[-1:]) * 10
        digit = num % 10

        ans = ""
        if billions:
            ans += self.numberToWords(billions)
            ans += " Billion"
        if millions:
            if ans:
                ans += " "
            ans += self.numberToWords(millions)
            ans += " Million"
        if thousands:
            if ans:
                ans += " "
            ans += self.numberToWords(thousands)
            ans += " Thousand"
        if hundreds:
            if ans:
                ans += " "
            ans += self.numberToWords(hundreds)
            ans += " Hundred"
        if 0 < tenth_plus_digit < 20:
            if ans:
                ans += " "
            ans += words[tenth_plus_digit]
        else:
            if tenth:
                if ans:
                    ans += " "
                ans += words[tenth]
            if digit:
                if ans:
                    ans += " "
                ans += words[digit]

        return ans
