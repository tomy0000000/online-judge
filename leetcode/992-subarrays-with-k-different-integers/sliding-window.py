from collections import Counter


class Solution:
    def counter_desc(self, c: Counter, item: int) -> None:
        if c[item] == 1:
            c.pop(item)
        else:
            c[item] -= 1

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        c = Counter()
        left = 0
        ans = 0
        base = 1
        for right in range(len(nums)):
            c[nums[right]] += 1

            if len(c) >= k:
                if len(c) > k:
                    base = 0
                while len(c) > k or (len(c) == k and c[nums[left]] > 1):
                    self.counter_desc(c, nums[left])
                    left += 1
                    if len(c) == k:
                        base += 1
                ans += base

        return ans
