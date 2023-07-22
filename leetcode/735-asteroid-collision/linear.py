# Let n be the length of asteroids
#
# Time: O(n)
# Space: O(1)


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        top_index = -1
        while len(asteroids) > -top_index:
            top = asteroids[top_index]
            top_2 = asteroids[top_index - 1]
            if top_2 > 0 and top < 0:
                size_top_2 = abs(top_2)
                size_top = abs(top)
                if size_top_2 < size_top:
                    asteroids.pop(top_index - 1)
                elif size_top_2 > size_top:
                    asteroids.pop(top_index)
                    top_index = -1 if top_index == -1 else top_index + 1
                else:
                    asteroids.pop(top_index - 1)
                    asteroids.pop(top_index)
                    top_index = -1 if top_index == -1 else top_index + 1
            else:
                top_index -= 1

        return asteroids
