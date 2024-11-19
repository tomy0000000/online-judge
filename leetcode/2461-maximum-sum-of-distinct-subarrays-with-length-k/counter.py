# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = 0

        counter = Counter()
        duplicates = 0
        summ = 0
        for n in nums[:k]:
            if counter[n] == 1:
                duplicates += 1
            counter[n] += 1
            summ += n

        if len(counter) == k:
            max_sum = max(max_sum, summ)

        for i in range(k, len(nums)):
            right = nums[i]
            if counter[right] == 1:
                duplicates += 1
            counter[right] += 1
            summ += right

            left = nums[i - k]
            counter[left] -= 1
            if counter[left] == 1:
                duplicates -= 1
            summ -= left

            if duplicates == 0:
                max_sum = max(max_sum, summ)

        return max_sum
