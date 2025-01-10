# Let n be the length of words1 and m be the length of words2
#
# Time: O(n + m)
# Space: O(1)

from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        universal_counter = Counter()
        for word2 in set(words2):
            counter = Counter()
            for c in word2:
                counter[c] += 1
                universal_counter[c] = max(universal_counter[c], counter[c])

        return [word1 for word1 in words1 if universal_counter <= Counter(word1)]
