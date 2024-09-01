# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []

        return [[original[i * n + j] for j in range(n)] for i in range(m)]
