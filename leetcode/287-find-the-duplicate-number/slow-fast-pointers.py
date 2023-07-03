# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        # The first loop bring fast pointer into cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # The second loop reset the slow pointer and ensure they meet at the start of the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
