# Let n be the length of the string s.
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def minOperations(self, s: str) -> int:
        counters = [Counter(), Counter()]
        for i, b in enumerate(s):
            counters[i % 2][b] += 1

        return min(
            counters[0]["1"] + counters[1]["0"], counters[0]["0"] + counters[1]["1"]
        )
