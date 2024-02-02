# Time: O(1)
# Space: O(1)


from bisect import bisect_left, bisect_right


class Solution:
    def __init__(self):
        self.comb = []
        for length in range(2, 10):
            for s in range(1, 11 - length):
                self.comb.append(int("".join(map(str, range(s, s + length)))))

    def sequentialDigits(self, low: int, high: int) -> list[int]:
        left = bisect_left(self.comb, low)
        right = bisect_right(self.comb, high)
        return self.comb[left:right]
