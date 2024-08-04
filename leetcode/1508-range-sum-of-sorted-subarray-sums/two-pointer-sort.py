# Let n be the length of the nums
#
# Time: O(n ^ 2 * log(n))
# Space: O(n ^ 2)


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sums = []
        for l in range(n):
            summ = 0
            for r in range(l + 1, n + 1):
                summ += nums[r - 1]
                sums.append(summ)
        sums.sort()
        return sum(sums[left - 1 : right]) % (10**9 + 7)
