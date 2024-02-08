# Time: O(n * sqrt(n))
# Space: O(n)


class Solution:
    def __init__(self):
        self.psns = [(n + 1) ** 2 for n in range(int(10000**0.5))]

    def numSquares(self, n: int) -> int:
        if n in self.psns:
            return 1

        mini = 1
        remains = set(n - item for item in self.psns)
        while remains:
            mini += 1

            if remains.intersection(self.psns):
                break

            remains = set(
                remain - psn for remain in remains for psn in self.psns if psn <= remain
            )

        return mini
