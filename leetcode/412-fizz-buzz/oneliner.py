# Time: O(n)
# Space: O(1)


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return [
            "FizzBuzz"
            if i % 15 == 0
            else "Fizz"
            if i % 3 == 0
            else "Buzz"
            if i % 5 == 0
            else str(i)
            for i in range(1, n + 1)
        ]
