# Let n be the length of s and m be the length of shifts.
#
# Time: O(n + m log m)
# Space: O(n)

from bisect import insort


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        offsets = []
        ends = []
        ptr = 0
        offset = 0
        shifts.sort()
        for start, end, direction in shifts:
            for i in range(ptr, start):
                offsets.append(offset)
                while ends and ends[0][0] <= i:
                    _, off = ends.pop(0)
                    offset -= off
            ptr = start
            if direction == 0:
                offset -= 1
                insort(ends, (end, -1))
            if direction == 1:
                offset += 1
                insort(ends, (end, 1))

        for i in range(ptr, len(s)):
            offsets.append(offset)
            while ends and i == ends[0][0]:
                _, off = ends.pop(0)
                offset -= off

        new_str = []
        for c, offset in zip(s, offsets):
            index = ord(c) - ord("a")
            index = (index + offset) % 26
            new_str.append(chr(index + ord("a")))

        return "".join(new_str)
