class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            ans = int("".join(list(str(x))[::-1]))
            return 0 if ans > 2147483647 else ans
        else:
            ans = int("".join(list(str(x)[1:])[::-1])) * -1
            return 0 if ans < -2147483648 else ans
