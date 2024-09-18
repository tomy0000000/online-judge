# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)

import functools


def cmp(a, b):
    comb1, comb2 = f"{a[0]}{b[0]}", f"{b[0]}{a[0]}"
    if comb1 > comb2:
        return -1
    if comb1 < comb2:
        return 1
    return 0


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        tuples = [(str(n), n) for n in nums]
        tuples.sort(key=functools.cmp_to_key(cmp))
        return str(int("".join([str(t[1]) for t in tuples])))
