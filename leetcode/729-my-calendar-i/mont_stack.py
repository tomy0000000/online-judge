from bisect import bisect_left


class MyCalendar:
    def __init__(self):
        self.data = []

    def book(self, start: int, end: int) -> bool:
        # Let n be the length of self.data
        #
        # Time: O(n log n)
        # Space: O(1)
        t = (start, end)
        pos = bisect_left(self.data, t)
        if (0 < pos and start < self.data[pos - 1][1]) or (
            pos < len(self.data) and self.data[pos][0] < end
        ):
            return False
        self.data.insert(pos, t)
        return True
