# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxi = 0
        for c in s:
            if c == "(":
                depth += 1
                maxi = max(maxi, depth)
            elif c == ")":
                depth -= 1
        return maxi
