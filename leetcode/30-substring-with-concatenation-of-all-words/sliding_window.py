# Let n be the length of s and m be the length of unique words.
#
# Time: O(n * m)
# Space: O(m)

from collections import Counter


class Solution:
    def counter_pop(self, counter: dict[str, int], item: str):
        if counter[item] == 1:
            del counter[item]
        else:
            counter[item] -= 1

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        c = Counter(words)
        c_backup = c.copy()
        ans = []
        l, r = 0, 0
        while r != len(s):
            sub = s[r : r + word_len]
            if sub in c:
                self.counter_pop(c, sub)
                r += word_len
                if not c:
                    ans.append(l)
                    if word_len == 1:
                        c[s[l : l + word_len]] += 1
                        l += word_len
                    else:
                        c = c_backup.copy()
                        l += 1
                        r = l
            else:
                c = c_backup.copy()
                l += 1
                r = l
        return ans
