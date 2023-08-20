# Let n be the length of s.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()
        substrings = set()
        begin = 0

        for i, c in enumerate(s):
            if c in used:
                substrings.add(s[begin:i])
                last_c_pos = used[c]
                for used_c in s[begin : last_c_pos + 1]:
                    used.pop(used_c)
                begin = last_c_pos + 1
            used[c] = i
        substrings.add(s[begin:])

        if not substrings:
            return 0

        return len(max(substrings, key=len))
