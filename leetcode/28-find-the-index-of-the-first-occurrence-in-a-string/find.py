# Let n be the length of haystack
#
# Time: O(n)
# Space: O(1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
