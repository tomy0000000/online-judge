# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            while left < right and s[left] == s[left + 1]:
                left += 1
            left += 1
            while left < right and s[right - 1] == s[right]:
                right -= 1
            right -= 1
        return max(right - left + 1, 0)
