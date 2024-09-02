# Let n be the length of chalk
#
# Time: O(n)
# Space: O(1)


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        n = len(chalk)
        summ = sum(chalk)
        k %= summ

        for i in range(n):
            if chalk[i] <= k:
                k -= chalk[i]
            else:
                return i
