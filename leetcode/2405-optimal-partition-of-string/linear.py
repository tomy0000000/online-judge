# Let n be the length of the string.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def partitionString(self, s: str) -> int:
        previous = set()
        split = 1
        for c in s:
            if c in previous:
                split += 1
                previous = set(c)
            else:
                previous.add(c)
        return split
