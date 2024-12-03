# Let n be the length of s
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        length = len(s)
        d = deque()
        space_ptr = len(spaces) - 1
        for i in range(length - 1, -1, -1):
            c = s[i]
            d.appendleft(c)
            if i == spaces[space_ptr]:
                d.appendleft(" ")
                space_ptr -= 1
        return "".join(d)
