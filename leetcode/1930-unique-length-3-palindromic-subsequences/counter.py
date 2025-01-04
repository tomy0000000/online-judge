# Let n be the length of s
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count_right = Counter(s[1:])
        count_left = Counter(s[0])
        palis = set()
        for c in s[1:-1]:
            if count_right[c] == 1:
                count_right.pop(c)
            else:
                count_right[c] -= 1
            for cc in count_left:
                if cc in count_right:
                    palis.add(f"{cc}{c}{cc}")
            count_left[c] += 1
        return len(palis)
