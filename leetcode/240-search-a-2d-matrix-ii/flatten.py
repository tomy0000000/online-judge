# Let n be the length matrix.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        flat = [n for row in matrix for n in row]
        return target in flat
