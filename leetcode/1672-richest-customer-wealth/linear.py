# Let n be the length of all accounts combined.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(m) for m in accounts)
