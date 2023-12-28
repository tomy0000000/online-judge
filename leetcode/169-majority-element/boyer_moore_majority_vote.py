# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = nums[0]
        for n in nums:
            if count == 0:
                candidate = n
                count += 1
            elif n == candidate:
                count += 1
            else:
                count -= 1
        return candidate
