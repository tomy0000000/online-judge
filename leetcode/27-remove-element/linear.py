# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        filtered = [n for n in nums if n != val]
        k = len(filtered)
        nums[:k] = filtered
        return k
