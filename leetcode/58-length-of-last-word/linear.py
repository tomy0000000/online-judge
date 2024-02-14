# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
