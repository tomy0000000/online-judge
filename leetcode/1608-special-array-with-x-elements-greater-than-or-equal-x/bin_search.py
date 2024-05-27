# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(1)

from bisect import bisect_left


class Solution:
    def count_larger_than_x(self, nums: list[int], x: int) -> int:
        return len(nums) - bisect_left(nums, x)

    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = self.count_larger_than_x(nums, mid)
            if cnt == mid:
                return mid
            elif cnt > mid:
                lo = mid + 1
            else:
                hi = mid
        return lo if self.count_larger_than_x(nums, lo) == lo else -1
