# Let w be the number of words and n be the length of s.
#
# Time: O(w + n)
# Space: O(1)


class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        return "".join(word[0] for word in words) == s
