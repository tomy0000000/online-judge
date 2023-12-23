# Let n be the length matrix.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        w = len(matrix)
        h = len(matrix[0])
        i, j = 0, 0
        while i < w:
            while j < h and matrix[i][j] < target:
                j += 1
            if j < h and matrix[i][j] == target:
                return True
            j = 0
            i += 1
        return False
