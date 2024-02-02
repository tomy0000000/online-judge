# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        groups = n // 3
        ans = []
        for i in range(groups):
            sub = nums[i * 3 : (i + 1) * 3]
            if max(sub) - min(sub) > k:
                return []
            ans.append(sub)
        return ans
