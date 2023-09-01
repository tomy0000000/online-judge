# Time: O(n)
# Space: O(1)


class Solution:
    def bit_num(self, n: int):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n >>= 1
        return count

    def countBits(self, n: int) -> list[int]:
        return [self.bit_num(i) for i in range(n + 1)]
