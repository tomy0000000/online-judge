# Let n be the length of happiness
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        return sum(
            max(n - i, 0) for i, n in enumerate(sorted(happiness)[: -k - 1 : -1])
        )
