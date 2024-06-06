# Let n be the length of nums
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        nums.sort()
        while nums:
            base = nums[0]
            for i in range(k):
                if base + i in nums:
                    nums.remove(base + i)
                else:
                    return False
        return True
