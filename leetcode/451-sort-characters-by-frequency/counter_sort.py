# Let n be the length of s
#
# Time: O(n log n)
# Space: O(1)


from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        chars = [(cnt, char) for char, cnt in Counter(s).items()]
        chars.sort(reverse=True)
        return "".join(f"{char*cnt}" for cnt, char in chars)
