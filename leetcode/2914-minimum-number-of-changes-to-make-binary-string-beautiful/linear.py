# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minChanges(self, s: str) -> int:
        prev = s[0]
        count = 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                prev = c
            else:
                if c != prev:
                    count += 1
        return count
