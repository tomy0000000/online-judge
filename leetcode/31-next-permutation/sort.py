# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n log n))


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        length = len(nums)
        if length == 1:
            return

        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.sort()
            return

        to_swap = i + 1
        while to_swap < length - 1 and nums[i] < nums[to_swap + 1]:
            to_swap += 1

        nums[i], nums[to_swap] = nums[to_swap], nums[i]
        nums[i + 1 :] = sorted(nums[i + 1 :])
