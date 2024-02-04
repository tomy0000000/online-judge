# Let n be the length of nums
#
# Time: O(n!)
# Space: O(n!)


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for perm in self.permute(nums[1:]):
            for i in range(len(perm) + 1):
                new_perm = perm.copy()
                new_perm.insert(i, nums[0])
                res.append(new_perm)
        return res
