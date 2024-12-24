# Let n be the length of heights and m be the length of queries.
#
# Time: O(n * log(n) + m * log(n))
# Space: O(n)

from bisect import bisect_right


class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        height_indexes = [(h, i) for i, h in enumerate(heights)]
        height_indexes.sort()

        for i, (b1, b2) in enumerate(queries):
            if b1 > b2:
                queries[i] = [b2, b1]

        ans = []
        for b1, b2 in queries:
            if b1 == b2 or heights[b1] < heights[b2]:
                ans.append(b2)
                continue

            index = bisect_right(height_indexes, heights[b1], key=lambda x: x[0])
            candidates = [t[1] for t in height_indexes[index:] if t[1] > b2]
            ans.append(min(candidates) if candidates else -1)

        return ans
