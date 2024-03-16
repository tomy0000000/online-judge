# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        prefix = [0]
        acc = 0
        for n in nums:
            acc += 1 if n == 0 else -1
            prefix.append(acc)

        locs = defaultdict(list)
        for i, s in enumerate(prefix):
            locs[s].append(i)

        maxi = 0
        for _, loc in locs.items():
            maxi = max(maxi, loc[-1] - loc[0])
        return maxi
