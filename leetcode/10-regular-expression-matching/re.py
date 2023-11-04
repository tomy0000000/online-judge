# Let n be the length of s.
#
# Time: O(n)
# Space: O(n)


import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while "**" in p:
            p = p.replace("**", "*")
        return re.fullmatch(p, s) is not None
