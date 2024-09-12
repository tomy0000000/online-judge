# Let n be length of words
#
# Time: O(n)
# Space: O(1)


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return sum(1 for word in words if all(c in allowed for c in word))
