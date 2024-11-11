# Let n be the length of intervals
#
# Time: O(n log(n))
# Space: O(1)


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        length = len(intervals)
        i = 0
        while i < length - 1:
            if intervals[i + 1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
                length -= 1
            else:
                i += 1
        return intervals
