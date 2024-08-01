# Let n be the length of details
#
# Time: O(n)
# Space: O(n)


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum(1 for p in details if int(p[11:13]) > 60)
