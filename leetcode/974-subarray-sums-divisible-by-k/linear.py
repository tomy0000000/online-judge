# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainders = Counter()
        remainders[0] += 1
        mod = 0
        ans = 0
        for n in nums:
            mod = (mod + n) % k
            ans += remainders[mod]
            remainders[mod] += 1
        return ans
