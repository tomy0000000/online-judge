# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        ptr = 0
        flip = 0
        ban_num = 0
        flip_bans = deque()

        while True:
            while ptr < len(nums) and nums[ptr] != ban_num:
                ptr += 1
                if flip_bans and ptr == flip_bans[0]:
                    flip_bans.popleft()
                    ban_num = int(not bool(ban_num))

            if ptr == len(nums):
                return flip

            if ptr + k > len(nums):
                return -1

            if ptr + k == len(nums):
                for i in range(ptr, ptr + k):
                    if flip_bans and i == flip_bans[0]:
                        flip_bans.popleft()
                        ban_num = int(not bool(ban_num))
                    if nums[i] != ban_num:
                        return -1
                return flip + 1

            flip += 1
            ban_num = int(not bool(ban_num))
            flip_bans.append(ptr + k)
