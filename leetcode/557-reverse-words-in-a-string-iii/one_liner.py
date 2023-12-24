# Let n be the number of words in s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split()])
