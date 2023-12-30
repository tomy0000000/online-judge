# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        prev, length = nums[0], 1
        pop_indexes = []
        for i in range(1, len(nums)):
            if nums[i] == prev:
                pop_indexes.append(i)
            else:
                prev = nums[i]
                length += 1

        for i in pop_indexes[::-1]:
            nums.pop(i)

        return length
