# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def makeFancyString(self, s: str) -> str:
        length = len(s)
        acc = 1
        char = s[0]
        i = 1
        while i < length:
            if s[i] != char:
                char = s[i]
                acc = 1
                i += 1
                continue

            if acc == 2:
                s = s[:i] + s[i + 1 :]
                length -= 1
                continue

            acc += 1
            i += 1

        return s
