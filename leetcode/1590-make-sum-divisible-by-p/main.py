# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        length = len(nums)
        target = sum(nums) % p

        if target == 0:
            return 0

        prev_mods = {0: -1}
        current = 0
        mini = length
        for i, n in enumerate(nums):
            current += n
            mod = current % p
            target_mod = (mod - target) % p

            if target_mod in prev_mods:
                mini = min(mini, i - prev_mods[target_mod])

            prev_mods[mod] = i

        return -1 if mini == length else mini
