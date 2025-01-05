# Let n be the length of s and m be the length of shifts.
#
# Time: O(n + m)
# Space: O(n)

from collections import defaultdict


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        offsets = defaultdict(int)
        for start, end, direction in shifts:
            if direction == 0:
                offsets[start] -= 1
                offsets[end + 1] += 1
            if direction == 1:
                offsets[start] += 1
                offsets[end + 1] -= 1

        new_str = []
        offset = 0
        for i, c in enumerate(s):
            off = offsets[i]
            offset += off
            index = ord(c) - ord("a")
            index = (index + offset) % 26
            new_str.append(chr(index + ord("a")))
        return "".join(new_str)
