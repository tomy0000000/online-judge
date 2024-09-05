# Time: O(1)
# Space: O(1)


class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        total = mean * (m + n)
        total_n = total - sum(rolls)
        if total_n < 1 * n or total_n > 6 * n:
            return []
        n_rolls = [total_n // n] * n
        remainds = total_n - sum(n_rolls)
        for i in range(remainds):
            n_rolls[i] += 1
        return n_rolls
