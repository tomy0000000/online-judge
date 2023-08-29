# Time: O(1)
# Space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int("".join(list(str(x))[::-1]))
            return 0 if ans > 2147483647 else ans
        else:
            ans = int("".join(list(str(x)[1:])[::-1])) * -1
            return 0 if ans < -2147483648 else ans
