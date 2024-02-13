# Let n be the length of words
#
# Time: O(n)
# Space: O(1)


class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
