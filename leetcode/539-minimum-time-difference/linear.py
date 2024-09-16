# Let n be the length of timePoints
#
# Time: O(n log n)
# Space: O(1)

from math import inf


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        timePoints.sort()
        timePoints.append(timePoints[0])
        min_diff = inf
        prev = None
        for t in timePoints:
            hour, minute = t.split(":")
            dt = int(hour) * 60 + int(minute)
            if prev is not None:
                diff_1 = abs(dt - prev)
                diff_2 = 1440 - diff_1
                diff = min(diff_1, diff_2)
                min_diff = min(min_diff, diff)
            prev = dt
        return min_diff
