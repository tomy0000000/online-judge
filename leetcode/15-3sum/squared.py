# Let n be the length of nums
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # This problem is has a lower bound of O(n^2)
        # so it's fine to sort the nums first
        nums.sort()

        ans = []
        # One loop to iterate through the nums
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            # Two pointers to find the other two numbers in one loop
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in ans:
                        ans.append(triplet)
                if total <= 0:
                    left += 1
                if total >= 0:
                    right -= 1

        return ans
