# Let n be the length of lights
#
# Time: O(n * log(n))
# Space: O(n)


class Solution:
    def brightestPosition(self, lights: list[list[int]]) -> int:
        marks = []
        for loc, radius in lights:
            marks.append((loc - radius, 0))
            marks.append((loc + radius, 1))
        marks.sort()

        max_bright_loc = None
        max_bright = 0
        brightness = 0
        for loc, event in marks:
            if event == 0:
                brightness += 1
                if brightness > max_bright:
                    max_bright = brightness
                    max_bright_loc = loc
            else:
                brightness -= 1

        return max_bright_loc
