# Let n be the length of text1 and m be the length of text2.
#
# Time: O(n * m)
# Space: O(n * m)

from functools import lru_cache


class Solution:
    @lru_cache(32768)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        if text1[-1] == text2[-1]:
            return self.longestCommonSubsequence(text1[:-1], text2[:-1]) + 1
        else:
            return max(
                self.longestCommonSubsequence(text1[:-1], text2),
                self.longestCommonSubsequence(text1, text2[:-1]),
            )
