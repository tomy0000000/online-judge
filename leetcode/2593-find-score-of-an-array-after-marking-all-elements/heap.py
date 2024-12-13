# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from heapq import heapify, heappop


class Solution:
    def findScore(self, nums: list[int]) -> int:
        marked = set()
        nums_indexed = [(n, i) for i, n in enumerate(nums)]
        heapify(nums_indexed)
        score = 0
        while nums_indexed:
            n, i = heappop(nums_indexed)
            if i in marked:
                continue

            marked.add(i - 1)
            marked.add(i)
            marked.add(i + 1)

            score += n
        return score
