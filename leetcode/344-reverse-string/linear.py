# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def reverseString(self, s: list[str]) -> None:
        length = len(s)
        for i in range(length // 2):
            s[i], s[length - i - 1] = s[length - i - 1], s[i]
