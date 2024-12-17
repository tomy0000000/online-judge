class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.arr = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        # Time: O(n)
        # Space: O(n)
        idKey -= 1
        self.arr[idKey] = value
        start = self.ptr
        while self.ptr < self.n and self.arr[self.ptr]:
            self.ptr += 1
        return self.arr[start : self.ptr]
