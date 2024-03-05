# Let n be the length of s
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def minimumLength(self, s: str) -> int:
        deq = deque()
        prev = "z"
        for c in s:
            if c != prev:
                deq.append((c, 1))
                prev = c
            else:
                _, count = deq.pop()
                deq.append((c, count + 1))

        while len(deq) > 2 and deq[0][0] == deq[-1][0]:
            deq.popleft()
            deq.pop()

        if len(deq) == 1:
            if deq[0][1] == 1:
                return 1
            else:
                return 0

        return sum(t[1] for t in deq)
