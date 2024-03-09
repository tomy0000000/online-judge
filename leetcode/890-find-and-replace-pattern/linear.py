# Let n be the length of words
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        matched = []
        for word in words:
            mapping = {}
            for c1, c2 in zip(word, pattern):
                if c1 in mapping:
                    if mapping[c1] != c2:
                        break
                else:
                    mapping[c1] = c2
            else:
                if len(set(mapping.values())) == len(mapping.values()):
                    matched.append(word)
        return matched
