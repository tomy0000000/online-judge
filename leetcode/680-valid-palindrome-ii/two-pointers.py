# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def validPalindrome(self, s: str, used: bool = False) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                if used:
                    return False
                else:
                    return self.validPalindrome(
                        s[left:right], True
                    ) or self.validPalindrome(s[left + 1 : right + 1], True)
            else:
                left += 1
                right -= 1
        return True
