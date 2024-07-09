# Let n be the length of customers
#
# Time: O(n)
# Space: O(1)


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        length = len(customers)
        start = customers[0][0]
        wait_times = 0
        cur = 0
        while cur < length:
            arr, t = customers[cur]
            end = max(arr, start) + t
            wait_times += end - arr
            start = end
            cur += 1
        return wait_times / length
