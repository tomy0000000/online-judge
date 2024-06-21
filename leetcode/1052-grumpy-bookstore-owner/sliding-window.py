# Let n be the length of customers and grumpy.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        left = 0
        right = minutes
        window = sum(
            c if grumpy[i] == 1 else 0 for i, c in enumerate(customers[:right])
        )
        maxi_window = window
        max_left = left
        max_right = right
        while right < len(customers):
            if grumpy[right] == 1:
                window += customers[right]
            if grumpy[left] == 1:
                window -= customers[left]
            left += 1
            right += 1
            if window > maxi_window:
                maxi_window = window
                max_left = left
                max_right = right

        satisfied = 0
        for i, c in enumerate(customers):
            if max_left <= i < max_right or grumpy[i] == 0:
                satisfied += c

        return satisfied
