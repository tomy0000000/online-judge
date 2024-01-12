# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len([c for c in s[: len(s) // 2].lower() if c in "aeiou"]) == len(
            [c for c in s[len(s) // 2 :].lower() if c in "aeiou"]
        )
