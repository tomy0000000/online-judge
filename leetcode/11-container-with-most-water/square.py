# Let n be the length of height
#
# Time: O(n ^ 2) -> will time out
# Space: O(1)


class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxi = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j:
                    continue

                w = abs(i - j)
                h = min(height[i], height[j])
                volume = w * h

                if volume > maxi:
                    maxi = volume

        return maxi
