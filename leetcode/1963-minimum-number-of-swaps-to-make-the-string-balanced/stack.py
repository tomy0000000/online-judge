# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        rear = len(s) - 1
        while s[rear] == "]":
            rear -= 1

        swap = 0
        opened = 0
        for c in s:
            if c == "[":
                opened += 1
                continue
            if c == "]":
                if opened:
                    opened -= 1
                else:
                    s[rear] = "]"
                    opened += 1
                    rear -= 1
                    while s[rear] == "]":
                        rear -= 1
                    swap += 1
        return swap
