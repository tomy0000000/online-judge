# Let n be the length of times
#
# Time: O(n)
# Space: O(n)

from heapq import heappop, heappush


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        heap = []
        for friend, (arr, leave) in enumerate(times):
            heappush(heap, (leave, 0, friend))
            heappush(heap, (arr, 1, friend))
        chairs = {}
        empties = []
        next_chair = 0
        while heap:
            t, action, friend = heappop(heap)
            if action == 0:
                chair = chairs[friend]
                heappush(empties, chair)
            if action == 1:
                if empties:
                    chair = heappop(empties)
                else:
                    chair = next_chair
                    next_chair += 1
                chairs[friend] = chair
                if friend == targetFriend:
                    return chair
