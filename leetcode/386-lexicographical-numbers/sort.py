# Time: O(n log n)
# Space: O(n)


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        return [int(num) for num in sorted(str(num) for num in range(1, n + 1))]
