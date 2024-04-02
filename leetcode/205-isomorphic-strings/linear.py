# Let n be the length of s and t
#
# Time: O(n)
# Space: O(1)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        for c1, c2 in zip(s, t):
            if c1 in maps:
                if maps[c1] != c2:
                    return False
            else:
                maps[c1] = c2
        chars = maps.values()
        return len(set(chars)) == len(chars)
