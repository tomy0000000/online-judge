# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefix_map = {0: -1}
        mask = 0
        longest = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                bit = "aeiou".index(c)
                mask ^= 2**bit

            if mask in prefix_map:
                prev = prefix_map[mask]
                longest = max(longest, i - prev)
            else:
                prefix_map[mask] = i

        return longest
