# Let n be the length of numbers
#
# Time: O(n)
# Space: O(1)


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        total = numbers[left] + numbers[right]
        while total != target:
            if total > target:
                right -= 1
            else:
                left += 1

            total = numbers[left] + numbers[right]

        return [left + 1, right + 1]
