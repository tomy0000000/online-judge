# Let n be the length of nums
#
# Time: O(n * log(n))
# Space: O(1)


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        ans = sum(nums[:2])
        maxi = -1
        for i in range(2, len(nums)):
            if nums[i] < ans:
                maxi = max(maxi, ans + nums[i])
            ans += nums[i]

        return maxi
