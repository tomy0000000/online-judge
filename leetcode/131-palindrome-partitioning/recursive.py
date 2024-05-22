# Let n be the length of s
#
# Time: O(2 ^ n)
# Space: O(2 ^ n)

from functools import cache


class Solution:
    @cache
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    @cache
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[]]

        p = []
        if self.isPalindrome(s):
            p.append((s,))
        for i in range(1, len(s)):
            s1, s2 = s[:i], s[i:]
            if not self.isPalindrome(s1):
                continue
            for p2 in self.partition(s2):
                p.append((s1,) + p2)

        return p
