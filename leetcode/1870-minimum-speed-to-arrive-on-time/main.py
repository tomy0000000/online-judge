# Let n be the length of dist.
#
# Time: O(n log n)
# Space: O(n)
import math


class Solution:
    def bin_search(self, dist: list[int], maxi: float, low: int, high: int):
        if low >= high:
            return low

        mid = (low + high) // 2
        total_time = self.calc_times(dist, mid)

        if low == high and total_time > maxi:
            return -1

        if total_time > maxi:
            return self.bin_search(dist, maxi, mid + 1, high)
        else:
            return self.bin_search(dist, maxi, low, mid)

    def calc_times(self, dist: list[int], speed: int):
        times = [math.ceil(d / speed) for d in dist]
        times[-1] = dist[-1] / speed
        total_times = sum(times)
        return total_times

    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        last_speed = int(dist[-1] / (hour - (len(dist) - 1))) + 1
        high = max(dist + [last_speed])
        res = self.bin_search(dist, hour, 1, high)
        return res
