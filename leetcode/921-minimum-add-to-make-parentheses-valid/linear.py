# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        moves = 0
        for c in s:
            if c == "(":
                count += 1
            if c == ")":
                if count:
                    count -= 1
                else:
                    moves += 1
        return moves + count
