# Let n be the length of word
#
# Time: O(n)
# Space: O(n)

from collections import Counter, defaultdict


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        rev_counter = defaultdict(set)
        for c, n in counter.items():
            rev_counter[n].add(c)

        press = 0
        multiplier = 1
        remains = 8
        for count in sorted(rev_counter, reverse=True):
            while rev_counter[count]:
                if remains == 0:
                    remains = 7
                    multiplier += 1
                else:
                    remains -= 1
                press += count * multiplier

        return press
