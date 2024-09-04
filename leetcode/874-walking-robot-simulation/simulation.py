# Let n be the length of commands
#
# Time: O(n)
# Space: O(1)


class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        x, y = 0, 0
        face = 0
        maxi_dist = 0
        o_set = set((x, y) for (x, y) in obstacles)
        for c in commands:
            if c == -1:
                face = 0 if face == 3 else face + 1
            elif c == -2:
                face = 3 if face == 0 else face - 1
            else:
                for _ in range(c):
                    next_x, next_y = x, y
                    if face == 0:
                        next_y += 1
                    elif face == 1:
                        next_x += 1
                    elif face == 2:
                        next_y -= 1
                    elif face == 3:
                        next_x -= 1
                    if (next_x, next_y) in o_set:
                        break
                    x, y = next_x, next_y
            maxi_dist = max(maxi_dist, x**2 + y**2)
        return maxi_dist
