# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dist = {}
        for i, c in enumerate(s):
            if c in dist:
                dist[c] = (i - dist[c][1] - 1, dist[c][1])
            else:
                dist[c] = (-1, i)

        return max(dist.values())[0]
