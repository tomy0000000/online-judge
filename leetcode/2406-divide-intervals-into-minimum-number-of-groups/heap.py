# Let n be the length of intervals
#
# Time: O(n log n)
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        rights = []
        group = 0
        for left, right in intervals:
            if rights and rights[0] < left:
                heappop(rights)
            else:
                group += 1
            heappush(rights, right)
        return group
