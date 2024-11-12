# Let n be the length of num
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        swap = None
        maxi = 0
        maxi_index = None
        for i in range(len(num) - 1, -1, -1):
            n = int(num[i])
            if n > maxi:
                maxi = n
                maxi_index = i
            if n < maxi:
                swap = (i, maxi_index)

        if swap:
            num[swap[0]], num[swap[1]] = num[swap[1]], num[swap[0]]

        return int("".join(num))
