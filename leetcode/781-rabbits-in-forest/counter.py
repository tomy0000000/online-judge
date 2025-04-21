# Let n be the length of answers
#
# Time: O(n)
# Space: O(n)

import math
from collections import Counter


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        counter = Counter(answers)
        num = 0
        for answer, count in counter.items():
            per_group = answer + 1
            num += math.ceil(count / per_group) * (answer + 1)
        return num
