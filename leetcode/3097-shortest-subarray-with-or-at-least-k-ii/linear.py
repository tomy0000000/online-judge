# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter
from functools import cache
from math import inf


class Solution:
    @cache
    def get_bits(self, n: int) -> Counter:
        counter = Counter()
        b = 1
        while b <= n:
            if n & b:
                counter[b] += 1
            b <<= 1
        return counter

    def get_int(self, counter: Counter) -> int:
        num = 0
        for n in counter:
            if counter[n]:
                num += n
        return num

    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 1

        left = 0
        counter = Counter()
        min_length = inf
        for right in range(len(nums)):
            counter += self.get_bits(nums[right])
            while self.get_int(counter) >= k:
                min_length = min(min_length, right - left + 1)
                counter -= self.get_bits(nums[left])
                left += 1
            if min_length == 1:
                break

        return -1 if min_length == inf else min_length
