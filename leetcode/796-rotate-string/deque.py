# Let n be the length of s
#
# Time: O(n^2)
# Space: O(n)

from collections import deque


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        queue = deque(s)
        goal_queue = deque(goal)
        for _ in range(len(queue)):
            if queue == goal_queue:
                return True
            queue.rotate()
        return False
