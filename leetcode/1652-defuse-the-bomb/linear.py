# Let n be the length of code.
#
# Time: O(n^2)
# Space: O(n)


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k > 0:
            return [sum(code[j % n] for j in range(i + 1, i + k + 1)) for i in range(n)]

        if k < 0:
            return [sum(code[j % n] for j in range(i + k, i)) for i in range(n)]

        return [0] * n
