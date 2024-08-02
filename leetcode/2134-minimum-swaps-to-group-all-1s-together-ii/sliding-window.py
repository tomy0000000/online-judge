class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        length = len(nums)
        width = sum(nums)
        if length == 1 or width <= 1 or length == width:
            return 0

        summ = sum(nums[:width])
        maxi = summ
        right = width
        for _ in range(length):
            left = (right - width) % length
            summ += nums[right] - nums[left]
            maxi = max(maxi, summ)
            right = (right + 1) % length
        return width - maxi
