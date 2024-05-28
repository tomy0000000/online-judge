# Let n be the length of s and t
#
# Time: O(n)
# Space: O(n)


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        edits = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]

        left = 0
        acc = 0
        maxi = 0
        for right in range(len(edits)):
            acc += edits[right]
            while acc > maxCost:
                acc -= edits[left]
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
