# Let n be the length of nums.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)

        low = 0
        steps = 0
        maxi = 1
        previous = nums[0]

        for high in range(1, len(nums)):
            target = nums[high]
            if target != previous:
                steps += (target - previous) * (high - low)
                while steps > k:
                    steps -= target - nums[low]
                    low += 1

            length = high - low + 1
            maxi = max(maxi, length)
            previous = target

        return maxi
