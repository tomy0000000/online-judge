# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        deque_p, deque_n = deque(), deque()

        for n in nums:
            if n > 0:
                deque_p.append(n)
            else:
                deque_n.append(n)

        ans = []
        for i in range(len(nums)):
            ans.append(deque_p.popleft() if i % 2 == 0 else deque_n.popleft())

        return ans
