# Let n be the length of height.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        l, r = 1, len(height) - 2
        left_max, right_max = height[0], height[-1]
        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max <= right_max:
                ans += left_max - height[l]
                l += 1
            else:
                ans += right_max - height[r]
                r -= 1
        return ans
