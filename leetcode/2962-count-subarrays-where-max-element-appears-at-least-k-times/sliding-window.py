# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maxi = max(nums)
        maxi_count = 0
        left = 0
        length = len(nums)
        results = 0
        for right in range(length):
            if nums[right] != maxi:
                continue

            maxi_count += 1
            if maxi_count < k:
                continue

            left_span = 1
            while nums[left] != maxi:
                left += 1
                left_span += 1
            right_span = length - right
            results += left_span * right_span

            left += 1
            maxi_count -= 1

        return results
