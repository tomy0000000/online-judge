# Let n be the length of words
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        length = len(words)
        ans = 0
        for i in range(length):
            for j in range(i + 1, length):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans
