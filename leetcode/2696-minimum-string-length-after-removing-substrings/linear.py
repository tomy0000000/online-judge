# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minLength(self, s: str) -> int:
        ab = s.find("AB")
        cd = s.find("CD")
        while ab != -1 or cd != -1:
            pos = max(ab, cd)
            s = s[:pos] + s[pos + 2 :]

            pos = min(ab, cd)
            if pos != -1:
                s = s[:pos] + s[pos + 2 :]

            ab = s.find("AB")
            cd = s.find("CD")

        return len(s)
