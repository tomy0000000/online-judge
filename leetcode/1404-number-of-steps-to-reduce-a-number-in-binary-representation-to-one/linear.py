# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        step = 0
        while num != 1:
            step += 1
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
        return step
