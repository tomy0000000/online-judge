# Let n be the length of meetings
#
# Time: O(n log n)
# Space: O(n)


from collections import deque
from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        heapify(available)
        usage = [0 for _ in range(n)]
        waiting = deque()
        end_heap = []
        for now, new_end_time in meetings:
            while end_heap and end_heap[0][0] <= now:
                prev_end_time, room = heappop(end_heap)
                if waiting:
                    length = waiting.popleft()
                    end_time = prev_end_time + length
                    usage[room] += 1
                    heappush(end_heap, (end_time, room))
                else:
                    heappush(available, room)

            if available:
                room = heappop(available)
                usage[room] += 1
                heappush(end_heap, (new_end_time, room))
            else:
                waiting.append(new_end_time - now)

        while waiting:
            prev_end_time, room = heappop(end_heap)
            length = waiting.popleft()
            end_time = prev_end_time + length
            usage[room] += 1
            heappush(end_heap, (end_time, room))

        return max(range(len(usage)), key=lambda x: usage[x])
