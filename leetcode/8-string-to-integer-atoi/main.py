# Let n be the length of s.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def myAtoi(self, s: str) -> int:
        chars = []
        for c in s:
            if c in " ":
                if chars:
                    break
                continue
            if c in "1234567890-+":
                if c in "+-" and chars:
                    break
                chars.append(c)
            else:
                break

        try:
            number = int("".join(chars))
        except ValueError:
            number = 0

        mini = -(2**31)
        maxi = 2**31 - 1
        if number < mini:
            return mini
        if number > maxi:
            return maxi
        return number
