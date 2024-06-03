# Let n be the length of s and m be the length of t
#
# Time: O(n + m)
# Space: O(1)


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ps, pt = 0, 0
        ls, lt = len(s), len(t)
        while ps < ls and pt < lt:
            if s[ps] == t[pt]:
                pt += 1
            ps += 1
        return lt - pt
