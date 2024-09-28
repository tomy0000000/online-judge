from collections import deque


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.data = deque()

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.data.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.data.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def isFull(self) -> bool:
        return len(self.data) == self.k
