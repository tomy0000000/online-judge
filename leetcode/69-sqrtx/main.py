# Let n be the length of s.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def bin_search(self, x: int, start: int, end: int):
        if x == 1:
            return 1

        print(start, end)
        if start + 1 == end:
            return start

        mid = (start + end) // 2
        if mid**2 == x:
            return mid

        if mid**2 > x:
            return self.bin_search(x, start, mid)
        else:
            return self.bin_search(x, mid, end)

    def mySqrt(self, x: int) -> int:
        return self.bin_search(x, 0, x)
