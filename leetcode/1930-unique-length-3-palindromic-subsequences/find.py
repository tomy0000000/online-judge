# Let n be the length of s
#
# Time: O(n)
# Space: O(1)

import string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in string.ascii_lowercase:
            left, right = s.find(c), s.rfind(c)
            if left != right:
                ans += len(set(s[left + 1 : right]))
        return ans
