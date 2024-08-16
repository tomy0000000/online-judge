# Let n be the length of arrays
#
# Time: O(n)
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        mins = [(arrays[0][0], 0)]
        maxs = [(-arrays[0][-1], 0)]
        for i, arr in enumerate(arrays):
            if i == 0:
                continue
            heappush(mins, (arr[0], i))
            heappush(maxs, (-arr[-1], i))

        mini, mini_i = heappop(mins)
        maxi, maxi_i = heappop(maxs)
        maxi *= -1

        if mini_i == maxi_i:
            next_mini = mins[0][0]
            next_maxi = -maxs[0][0]
            if next_mini - mini > maxi - next_maxi:
                maxi, maxi_i = heappop(maxs)
                maxi *= -1
            else:
                mini, mini_i = heappop(mins)

        return maxi - mini
