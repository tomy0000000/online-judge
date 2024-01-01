# Let n be the length of g, m be the length of s
#
# Time: O(nlogn + mlogm)
# Space: O(1)


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        ans = 0
        while g and s:
            g_top = g[-1]
            s_top = s[-1]
            if s_top < g_top:
                s.pop()
            else:
                g.pop()
                s.pop()
                ans += 1
        return ans
