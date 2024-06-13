# Let n be the max of len(seats) and len(students).
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))
