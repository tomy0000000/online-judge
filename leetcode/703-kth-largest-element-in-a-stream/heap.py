# Time: O(n)
# Space: O(1)


from heapq import heapify, heappop, heappush, heappushpop


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heappushpop(self.heap, val)
        else:
            heappush(self.heap, val)
        return self.heap[0]
