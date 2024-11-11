# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        summ = 0
        sum_counter = Counter({0: 1})
        ans = 0
        for n in nums:
            summ += n
            target = summ - k
            ans += sum_counter[target]
            sum_counter[summ] += 1
        return ans
