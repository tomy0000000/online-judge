# Let n be the length of items and m be the length of queries
#
# Time: O(n * log(n) + m * log(n))
# Space: O(n)

from bisect import bisect_left


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        max_beauty = {0: 0}
        keys = [0]
        maxi = 0

        for p, b in items:
            if b > maxi:
                max_beauty[p] = b
                keys.append(p)
                maxi = b

        ans = []
        for q in queries:
            key = bisect_left(keys, q)
            if key == len(keys) or q < keys[key]:
                key -= 1
            ans.append(max_beauty[keys[key]])
        return ans
