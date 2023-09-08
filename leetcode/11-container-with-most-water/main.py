# Let n be the length of height
#
# Time: O(n)
# Space: O(1)


class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxi = 0
        left = 0
        right = len(height) - 1

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            volume = w * h

            if volume > maxi:
                maxi = volume

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxi
