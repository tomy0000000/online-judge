# Let n be the length of points.
#
# Time: O(n ^ 2)
# Space: O(n)

from bisect import insort


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        mont = []
        for x, y in points:
            dist = x**2 + y**2
            insort(mont, (dist, x, y))
        return [(x, y) for (dist, x, y) in mont[:k]]
