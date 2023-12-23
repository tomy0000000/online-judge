# Let n be the length of the path
#
# Time: O(n)
# Space: O(n)


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(x, y)}
        for dir in path:
            if dir == "N":
                x += 1
            if dir == "S":
                x -= 1
            if dir == "E":
                y += 1
            if dir == "W":
                y -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False
