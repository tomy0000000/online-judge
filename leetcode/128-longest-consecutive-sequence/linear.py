# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert to set
        nums = set(nums)

        max_length = 0
        for n in nums:
            # We want to only count from the head
            if n - 1 in nums:
                continue

            # Start counting
            current = n
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1

            # Compare against the current max length
            max_length = max(max_length, length)

        return max_length
