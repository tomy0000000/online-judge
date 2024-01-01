# Let n be the length of g, m be the length of s
#
# Time: O(nlogn + mlogm)
# Space: O(1)


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        ans = 0
        g_ptr, s_ptr = len(g) - 1, len(s) - 1
        while g_ptr >= 0 and s_ptr >= 0:
            if s[s_ptr] < g[g_ptr]:
                s_ptr -= 1
            else:
                g_ptr -= 1
                s_ptr -= 1
                ans += 1
        return ans
