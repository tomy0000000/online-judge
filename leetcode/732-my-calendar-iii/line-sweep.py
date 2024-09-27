from collections import defaultdict


class MyCalendarThree:
    def __init__(self):
        self.data = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        # Let n be the length of self.data
        #
        # Time: O(n log n)
        # Space: O(n)
        self.data[startTime] += 1
        self.data[endTime] -= 1
        count = 0
        maxi = 0
        for i in sorted(self.data):
            count += self.data[i]
            maxi = max(maxi, count)
        return maxi
