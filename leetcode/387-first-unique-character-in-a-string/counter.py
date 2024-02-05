# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = set(c for c, n in Counter(s).items() if n == 1)
        for i in range(len(s)):
            if s[i] in unique:
                return i
        return -1
