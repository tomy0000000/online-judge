# Let n be the length of nums
#
# Time: O(n^2 * 2^n)
# Space: O(n * 2^n)

from typing import Optional


class Solution:
    def subsetsWithDup(
        self, nums: list[int], exists: Optional[set[list[int]]] = None
    ) -> list[list[int]]:
        if not nums:
            return exists

        n = nums.pop()
        exists = set([tuple()]) if not exists else exists
        exists.update([tuple(sorted(sub + (n,))) for sub in exists])

        return self.subsetsWithDup(nums, exists)
