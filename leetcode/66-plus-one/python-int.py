# Let n be the length of the digits
#
# Time: O(1)
# Space: O(1)


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits))) + 1
        return list(map(int, list(str(num))))
