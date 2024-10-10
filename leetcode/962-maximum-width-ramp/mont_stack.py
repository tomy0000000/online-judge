# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = []
        for i, n in enumerate(nums):
            if not stack or n < nums[stack[-1]]:
                stack.append(i)
            if n == 0:
                break

        maxi = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                maxi = max(maxi, j - stack.pop())

        return maxi
