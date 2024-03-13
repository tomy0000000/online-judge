# Time: O(n)
# Space: O(1)


class Solution:
    def pivotInteger(self, n: int) -> int:
        summ = (1 + n) * n // 2
        acc = 0
        for i in range(1, n + 1):
            acc += i
            if (summ + i) % 2 != 0:
                continue
            target = (summ + i) // 2
            if acc == target:
                return i
        return -1
