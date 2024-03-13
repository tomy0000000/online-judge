# Time: O(1)
# Space: O(1)


from math import sqrt


class Solution:
    def pivotInteger(self, n: int) -> int:
        summ = (1 + n) * n // 2
        root = sqrt(summ)
        return int(root) if int(root) == root else -1
