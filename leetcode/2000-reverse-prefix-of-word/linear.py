# Let n be the length of word
#
# Time: O(n)
# Space: O(n)


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        loc = word.find(ch)
        if loc == -1:
            return word
        prefix = word[loc::-1]
        postfix = word[loc + 1 :]
        return f"{prefix}{postfix}"
