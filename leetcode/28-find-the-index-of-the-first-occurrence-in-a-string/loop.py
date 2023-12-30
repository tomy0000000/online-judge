# Let n be the length of haystack
#
# Time: O(n)
# Space: O(1)


class Solution:
    def strStr(self, haystack, needle):
        n, h = len(needle), len(haystack)
        for i in range(h - n + 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
