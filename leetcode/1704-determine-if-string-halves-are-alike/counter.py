# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


from collections import Counter


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        c1, c2 = Counter(s[:mid].lower()), Counter(s[mid:].lower())
        vca, vcb = 0, 0
        for v in ("a", "e", "i", "o", "u"):
            vca += c1[v]
            vcb += c2[v]
        return vca == vcb
