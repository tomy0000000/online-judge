# Time: O(n)
# Space: O(n)


class Solution:
    fib_cache = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.fib_cache:
            return self.fib_cache[n]

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.fib_cache[n] = result

        return result
