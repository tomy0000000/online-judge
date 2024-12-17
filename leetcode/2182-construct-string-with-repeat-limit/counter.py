# Let n be the length of s
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        new_str = ""
        chars = sorted(counter.keys(), reverse=True)
        for i, c in enumerate(chars):
            next_index = i + 1
            next_c = None
            if next_index < len(chars):
                next_c = chars[next_index]

            while counter[c]:
                if counter[c] <= repeatLimit:
                    new_str += c * counter[c]
                    counter.pop(c)
                    break

                new_str += c * repeatLimit
                counter[c] -= repeatLimit
                if next_c is not None and counter[next_c]:
                    new_str += next_c
                    counter[next_c] -= 1
                    if counter[next_c] == 0:
                        next_index += 1
                        if next_index < len(chars):
                            next_c = chars[next_index]
                else:
                    break
        return new_str
