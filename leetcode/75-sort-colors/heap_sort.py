# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(1)


from heapq import heapify, heappop


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        heapify(nums)
        nums += [heappop(nums) for _ in range(len(nums))]
