# Let n be the length of nums.
#
# Time: O(n)
# Space: O(n)


from functools import cache


class Solution:
    nums: list[int]

    @cache
    def _rob(self, cur: int, prev_robbed: bool, robbed: int) -> int:
        if cur == len(self.nums):
            return robbed

        ans = []
        if not prev_robbed:
            ans.append(self._rob(cur + 1, True, robbed + self.nums[cur]))

        ans.append(self._rob(cur + 1, False, robbed))
        return max(ans)

    def rob(self, nums: list[int]) -> int:
        self.nums = nums
        return self._rob(0, False, 0)
