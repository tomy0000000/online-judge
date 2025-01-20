# Let m be the number of rows and n be the number of columns.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [set(row) for row in mat]
        cols = [set(mat[i][j] for i in range(m)) for j in range(n)]

        set_dict = {}
        for i in range(m):
            for j in range(n):
                set_dict[mat[i][j]] = [rows[i], cols[j]]

        for i, n in enumerate(arr):
            for s in set_dict[n]:
                s.remove(n)
                if not s:
                    return i

        return -1
