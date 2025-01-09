# Let n be the length of words
#
# Time: O(n)
# Space: O(1)


class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))
