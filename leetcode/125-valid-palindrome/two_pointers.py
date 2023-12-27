# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = set(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        )  # a-z + A-Z + 0-9
        left = 0
        right = len(s) - 1

        while True:
            while left < len(s) and s[left] not in valid_chars:
                left += 1

            while 0 <= right and s[right] not in valid_chars:
                right -= 1

            if right <= left:
                return True

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
