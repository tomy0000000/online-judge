# Let n be the length of s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        left = 0
        longest = 0
        for right, c in enumerate(s):
            if c not in freqs:
                freqs[c] = 1
            else:
                freqs[c] += 1

            dist = right - left + 1
            cost = dist - max(freqs.values())

            if cost > k:
                freqs[s[left]] -= 1
                left += 1
            else:
                longest = max(longest, dist)

        return longest
