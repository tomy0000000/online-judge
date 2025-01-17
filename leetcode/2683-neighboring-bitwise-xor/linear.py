# Let n be the length of derived
#
# Time: O(n)
# Space: O(1)


class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return sum(derived) % 2 == 0
