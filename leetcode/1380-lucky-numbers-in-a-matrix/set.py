# Let n be the number of elements in the matrix
#
# Time: O(n)
# Space: O(n)


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        minis = set(min(row) for row in matrix)
        maxis = set(max(row[i] for row in matrix) for i in range(len(matrix[0])))
        return minis & maxis
