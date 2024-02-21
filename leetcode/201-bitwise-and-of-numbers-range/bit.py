# Time: O(1)
# Space: O(1)


from math import log2


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0

        xnor = ~(left ^ right)
        aand = left & right

        mask = 2 ** int(log2(right))
        ans = 0
        while True:
            if aand & mask:
                ans += mask
            if not xnor & mask:
                break
            mask >>= 1
        return ans
