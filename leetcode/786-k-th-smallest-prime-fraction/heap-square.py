# Let n be the length of arr
#
# Time: O(n ^ 2)
# Space: O(k)

from heapq import heappush, heappushpop


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        length = len(arr)
        heap = []
        for i in range(length):
            for j in range(i + 1, length):
                if len(heap) == k:
                    heappushpop(heap, (-arr[i] / arr[j], arr[i], arr[j]))
                else:
                    heappush(heap, (-arr[i] / arr[j], arr[i], arr[j]))
        return heap[0][1:]
