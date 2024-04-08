# Let n be the length of students and sandwiches
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        d = deque(students)
        sandwiches.reverse()

        while True:
            prev = len(d)
            for _ in range(len(d)):
                pref = d.popleft()
                if pref == sandwiches[-1]:
                    sandwiches.pop()
                else:
                    d.append(pref)
            if len(d) == prev:
                break

        return len(d)
