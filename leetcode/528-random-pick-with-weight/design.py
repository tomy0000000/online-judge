# Let n be the length of w
#
# Time: O(n log n)
# Space: O(n)

import random
from bisect import bisect_left


class Solution:
    def __init__(self, w: list[int]):
        self.acc = [w[0]]
        for weight in w[1:]:
            self.acc.append(self.acc[-1] + weight)

    def pickIndex(self) -> int:
        sample = random.randrange(1, self.acc[-1] + 1)
        return bisect_left(self.acc, sample)
