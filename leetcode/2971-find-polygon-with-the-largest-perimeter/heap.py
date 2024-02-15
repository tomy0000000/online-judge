# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


from heapq import heapify, heappop


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        summ = sum(nums)
        heap = [-n for n in nums]
        heapify(heap)

        while True:
            if not heap:
                return -1

            maxi = -heap[0]
            if summ - maxi <= maxi:
                heappop(heap)
                summ -= maxi
            else:
                break

        return summ
