# Let n be the length of ransomNote, and m be the length of magazine.
#
# Time: O(n + m)
# Space: O(1)

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)
