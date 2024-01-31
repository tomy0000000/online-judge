# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Make non-positive numbers some random number that are not within the anwer scope
        # use n + 1 here
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            # Ignore out-of-scope nums marked in first loop
            if abs(nums[i]) > n:
                continue

            # Get the number
            # They may be negative, so restore them back with abs
            # Switch to 0-index by minus 1
            index_to_marked_exist = abs(nums[i]) - 1

            # Toggle the number at the index to negative
            # To mark the number as exists
            nums[index_to_marked_exist] = -abs(nums[index_to_marked_exist])

        # All numbers are supposed to be negative
        # If the number is positive, it means the index number is missing
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # All numbers existed
        return n + 1
