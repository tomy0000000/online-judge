# Let n be the length of nums
#
# Time: O(2 ^ n)
# Space: O(1)

from functools import reduce


class Solution:
    def combinations(
        self,
        target: int,
        remains: list[int],
        curr: int = 0,
    ) -> int:
        if not remains:
            return int(curr == target)

        count = 0

        # Pick one
        n = remains.pop()

        # Not Choose
        count += self.combinations(target, remains, curr)

        # Choose
        prev_curr = curr
        curr |= n
        count += self.combinations(target, remains, curr)
        curr = prev_curr

        # Put back
        remains.append(n)

        return count

    def countMaxOrSubsets(self, nums: list[int]) -> int:
        return self.combinations(reduce(lambda a, b: a | b, nums), nums)
