# Let n be the length of heights
#
# Time: O(n * log(n))
# Space: O(n)


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        return sum(int(h != eh) for h, eh in zip(heights, sorted(heights)))
