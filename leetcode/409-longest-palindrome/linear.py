# Let n be the length of s
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        odd = False
        for c, n in counter.items():
            ans += n
            if n % 2 == 1:
                ans -= 1
                odd = True
        return ans + int(odd)
