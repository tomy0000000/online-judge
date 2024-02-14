# Let n be the length of s
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def is_palindromic(self, s: str) -> bool:
        return s == s[::-1]

    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        ans = self.countSubstrings(s[:-1])
        for i in range(len(s) - 1, -1, -1):
            if self.is_palindromic(s[i:]):
                ans += 1
        return ans
