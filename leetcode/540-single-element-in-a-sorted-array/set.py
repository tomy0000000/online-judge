# Let n be the length of nums.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        c = set()
        for n in nums:
            if n in c:
                c.remove(n)
            else:
                c.add(n)
        return c.pop()
