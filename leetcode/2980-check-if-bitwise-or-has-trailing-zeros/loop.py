# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        even = False
        for n in nums:
            if n % 2 == 0:
                if not even:
                    even = True
                else:
                    return True
        return False
