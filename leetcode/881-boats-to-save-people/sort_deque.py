# Let n be the length of people
#
# Time: O(n log n)
# Space: O(n)

from collections import deque


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people = deque(sorted(people))
        boat = 0
        length = len(people)
        while length:
            boat += 1
            if length > 1 and people[0] + people[-1] <= limit:
                people.popleft()
                length -= 1
            people.pop()
            length -= 1

        boat += length

        return boat
