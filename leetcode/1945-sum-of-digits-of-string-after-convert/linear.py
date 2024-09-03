# Time: O(k)
# Space: O(1)


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        chars = list(s)
        nums = list(map(lambda c: ord(c) - 96, chars))
        digits = int("".join(str(num) for num in nums))
        for _ in range(k):
            digits = sum(map(int, list(str(digits))))
        return digits
