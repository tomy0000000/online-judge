# Let n be the length of intervals
#
# Time: O(n)
# Space: O(n)

from bisect import bisect_left, bisect_right


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # Empty intervals
        if not intervals:
            return [newInterval]

        start, end = None, None
        for i, (left, right) in enumerate(intervals):
            if left <= newInterval[0] <= newInterval[1] <= right:
                # Already contained
                return intervals
            if left <= newInterval[0] <= right:
                start = i
                continue
            if left <= newInterval[1] <= right:
                end = i
                break
            if newInterval[1] < left:
                break

        # Not overlapping any segment
        if start is None and end is None:
            in_left = bisect_left(intervals, newInterval[0], key=lambda x: x[0])
            in_right = bisect_right(intervals, newInterval[1], key=lambda x: x[1])
            del intervals[in_left:in_right]
            intervals.insert(in_left, newInterval)
            return intervals

        # Overlapped on right
        if start is None:
            in_left = bisect_right(intervals, newInterval[0], key=lambda x: x[1])
            del intervals[in_left:end]
            intervals[in_left][0] = newInterval[0]
            return intervals

        # Overlapped on left
        if end is None:
            intervals[start][1] = newInterval[1]
            in_right = bisect_right(intervals, newInterval[1], key=lambda x: x[1])
            del intervals[start + 1 : in_right]
            return intervals

        # Overlapped on both side
        intervals[start][1] = intervals[end][1]
        del intervals[start + 1 : end + 1]

        return intervals
