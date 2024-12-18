# Let n be the length of deliciousness
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        powers_of_two = [
            1,
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512,
            1024,
            2048,
            4096,
            8192,
            16384,
            32768,
            65536,
            131072,
            262144,
            524288,
            1048576,
            2097152,
        ]
        ans = 0
        counter = Counter(deliciousness)
        for d, count in counter.items():
            for pt in powers_of_two:
                target_d = pt - d
                if target_d == d:
                    ans += count * (count - 1)
                elif target_d in counter:
                    ans += count * counter[target_d]
        return ans // 2 % (10**9 + 7)
