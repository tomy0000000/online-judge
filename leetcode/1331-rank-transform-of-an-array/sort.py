# Let n be the length of arr
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ranks = {n: r for r, n in enumerate(sorted(set(arr)))}
        return [ranks[n] + 1 for n in arr]
