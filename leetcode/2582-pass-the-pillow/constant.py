# Time: O(1)
# Space: O(1)


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        factor = 2 * (n - 1)
        tmp = (time + 1) % factor
        tmp = factor if tmp == 0 else tmp
        return 2 * n - tmp if tmp > n else tmp
