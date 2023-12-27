# Let n be the length of word1 and word2 combined.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)
