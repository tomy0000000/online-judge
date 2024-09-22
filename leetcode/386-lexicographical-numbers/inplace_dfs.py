# Time: O(n)
# Space: O(1)


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        here = 1
        for _ in range(n):
            result.append(here)
            if here * 10 <= n:
                here *= 10
            else:
                while here % 10 == 9 or here + 1 > n:
                    here //= 10
                here += 1
        return result
