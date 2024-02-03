# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
