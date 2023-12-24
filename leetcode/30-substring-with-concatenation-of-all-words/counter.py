# Let n be the length of s and m be the length of unique words.
#
# Time: O(n * m)
# Space: O(m)

from collections import Counter


class Solution:
    def chunk_string(self, string: str, length: int) -> list[str]:
        return (string[0 + i : length + i] for i in range(0, len(string), length))

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        target_len = len(words) * word_len
        c = Counter(words)
        ans = []
        for index in range(len(s) - target_len + 1):
            sub = s[index : index + target_len]
            if c == Counter(self.chunk_string(sub, word_len)):
                ans.append(index)
        return ans
