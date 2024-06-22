# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_inds = [-1] + [i for i, n in enumerate(nums) if n % 2 == 1] + [len(nums)]
        count = 0
        for i in range(1, len(odd_inds) - k):
            count += (odd_inds[i] - odd_inds[i - 1]) * (
                odd_inds[i + k] - odd_inds[i + k - 1]
            )
        return count
