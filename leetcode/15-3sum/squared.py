# Let n be the length of nums
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplet = (nums[i], nums[left], nums[right])
                    if triplet not in ans:
                        ans.add(triplet)
                if total <= 0:
                    left += 1
                if total >= 0:
                    right -= 1

        return ans
