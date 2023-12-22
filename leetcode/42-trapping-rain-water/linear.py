# Let n be the length of height.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def _trap(self, height: list[int]) -> tuple[int, int]:
        ans = 0
        maxi = 0
        maxi_i = -1
        for i, h in enumerate(height):
            if maxi == 0:
                maxi = h
                maxi_i = i
                continue
            if h >= maxi:
                store_h = min(h, maxi)
                for store_i in range(maxi_i + 1, i):
                    ans += store_h - height[store_i]
                maxi = h
                maxi_i = i
        return ans, maxi_i

    def trap(self, height: list[int]) -> int:
        ans, last_bound = self._trap(height)
        if last_bound != len(height) - 1:
            bound = height[last_bound:]
            ans += self._trap(bound[::-1])[0]
        return ans
