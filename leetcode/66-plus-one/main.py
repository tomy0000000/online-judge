# Let n be the length of the digits
#
# Time: O(n)
# Space: O(1)


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ptr = len(digits) - 1
        while ptr >= 0 and digits[ptr] == 9:
            digits[ptr] = 0
            ptr -= 1
        if ptr >= 0:
            digits[ptr] += 1
        else:
            digits.insert(0, 1)
        return digits
