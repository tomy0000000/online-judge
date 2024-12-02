# Let n be the length of sentence and m be the length of searchWord
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i + 1
        return -1
