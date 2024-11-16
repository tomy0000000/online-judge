# Let n be the length of nums
#
# Time: O(n * k)
# Space: O(1)


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        left, right = 0, 0
        n = len(nums)
        invalid = 0
        result = []

        if k == 1:
            if invalid == 0:
                result.append(max(nums[left : right + 1]))
            else:
                result.append(-1)

        for i in range(n - 1):
            # left
            if i >= k - 1:
                if nums[left] + 1 != nums[left + 1]:
                    invalid -= 1
                left += 1

            # right
            right += 1
            if nums[right - 1] + 1 != nums[right]:
                invalid += 1

            # check valid
            if i >= k - 2:
                if invalid == 0:
                    result.append(max(nums[left : right + 1]))
                else:
                    result.append(-1)

        return result
