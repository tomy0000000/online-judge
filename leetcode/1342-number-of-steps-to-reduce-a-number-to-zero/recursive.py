# Let n be the value of num.
#
# Time: O(log(n))
# Space: O(1)

from functools import cache


class Solution:
    @cache
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return self.numberOfSteps(num // 2 if num % 2 == 0 else num - 1) + 1
