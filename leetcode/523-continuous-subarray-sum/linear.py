# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        remainders = {0: -1}
        mod = 0
        for i, n in enumerate(nums):
            mod = (mod + n) % k
            if mod in remainders:
                if i - remainders[mod] >= 2:
                    return True
            else:
                remainders[mod] = i
        return False
