# Let n be the length of A and B
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        c = []
        counter = Counter()
        acc = 0
        for a_n, b_n in zip(A, B):
            counter[a_n] += 1
            counter[b_n] += 1
            for n in set([a_n, b_n]):
                if counter[n] == 2:
                    acc += 1
            c.append(acc)
        return c
