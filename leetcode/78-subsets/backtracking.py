# Let n be the length of nums
#
# Time: O(n * 2^n)
# Space: O(n * 2^n)

from typing import Optional


class Solution:
    def subsets(
        self, nums: list[int], exists: Optional[list[list[int]]] = None
    ) -> list[list[int]]:
        if not nums:
            return exists

        n = nums.pop()
        exists = [[]] if not exists else exists
        exists.extend([sub + [n] for sub in exists])

        return self.subsets(nums, exists)
