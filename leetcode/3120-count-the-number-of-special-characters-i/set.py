# Let n be the length of word
#
# Time: O(n)
# Space: O(1)

import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        return sum(
            1 for c in string.ascii_lowercase if c in chars and c.upper() in chars
        )
