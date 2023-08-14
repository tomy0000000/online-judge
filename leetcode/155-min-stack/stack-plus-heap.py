import heapq


class MinStack:
    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)

    def pop(self) -> None:
        removed = self.stack.pop()
        self.heap.remove(removed)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]
