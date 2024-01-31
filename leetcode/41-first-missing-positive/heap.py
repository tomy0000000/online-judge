# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


from heapq import heapify, heappop


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        positives = [n for n in nums if n > 0]
        at_most = len(positives) + 1
        filtered = [n for n in positives if n < at_most]
        heapify(filtered)

        if not filtered:
            return 1

        prev, current = 0, heappop(filtered)
        while prev + 1 == current or prev == current:
            if not filtered:
                return current + 1
            prev, current = current, heappop(filtered)

        return prev + 1
