# Let n be the length of x.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
