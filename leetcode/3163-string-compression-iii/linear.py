# Let n be the length of word
#
# Time: O(n)
# Space: O(n)


class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        char = word[0]
        count = 0
        for c in word:
            if count == 9:
                comp += f"{count}{char}"
                char = c
                count = 0
            if c == char:
                count += 1
            else:
                comp += f"{count}{char}"
                char = c
                count = 1
        comp += f"{count}{char}"
        return comp
