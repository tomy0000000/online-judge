# Let n be the length of position and speed
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)
