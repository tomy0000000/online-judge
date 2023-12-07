# Let n be the length of position and speed
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            remain = target - p
            t = remain / s
            cars.append((p, s, t))

        cars.sort(key=lambda x: x[0], reverse=True)

        cur = 0
        fleet = 0
        for c in cars:
            if c[2] > cur:
                cur = c[2]
                fleet += 1
        return fleet
