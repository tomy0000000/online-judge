from collections import defaultdict


class MyCalendarTwo:
    def __init__(self):
        self.data = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        # Let n be the length of self.data
        #
        # Time: O(n log n)
        # Space: O(n)
        self.data[start] += 1
        self.data[end] -= 1
        count = 0
        for i in sorted(self.data):
            count += self.data[i]
            if count == 3:
                self.data[start] -= 1
                self.data[end] += 1
                return False
        return True
