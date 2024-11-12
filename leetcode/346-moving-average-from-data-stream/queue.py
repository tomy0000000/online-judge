# Let n be size
#
# Time: O(1)
# Space: O(n)

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.max_size = size
        self.size = 0
        self.queue = deque()
        self.summ = 0

    def next(self, val: int) -> float:
        if self.size == self.max_size:
            self.summ -= self.queue.popleft()
            self.size -= 1
        self.queue.append(val)
        self.size += 1
        self.summ += val
        return self.summ / len(self.queue)
