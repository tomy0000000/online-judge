# Let n be the length of height.
#
# Time: O(n ^ 2)
# Space: O(n)

from bisect import bisect_right


class Solution:
    def _trap(self, height: list[int]) -> tuple[int, int]:
        ans = 0
        mont = []
        for i, h in enumerate(height):
            index = bisect_right(mont, (h, i))
            if not mont or index != len(mont):
                mont.insert(index, (h, i))
            else:
                left_h, left_i = mont[-1]
                store_h = min(h, left_h)
                for store_i in range(left_i + 1, i):
                    ans += store_h - height[store_i]
                mont = [(h, i)]
        last_bound = mont[-1][1]
        return ans, last_bound

    def trap(self, height: list[int]) -> int:
        ans, last_bound = self._trap(height)
        if last_bound != len(height) - 1:
            bound = height[last_bound:]
            ans += self._trap(bound[::-1])[0]
        return ans
