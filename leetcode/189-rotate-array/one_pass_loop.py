# Let n be the length of the input list
#
# Time: O(n)
# Space: O(1)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        front = nums[-k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = front[i]
