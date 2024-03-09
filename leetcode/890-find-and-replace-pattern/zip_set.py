# Let n be the length of words
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        matched = []
        for word in words:
            if len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern))):
                matched.append(word)
        return matched
