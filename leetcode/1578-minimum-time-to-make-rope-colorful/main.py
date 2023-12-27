# Let n be the length of colors
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        color = ""
        maxi = 0
        summ = 0
        ans = 0
        n = len(colors)
        for i, (c, t) in enumerate(zip(colors, neededTime)):
            if c == color:
                maxi = t if t > maxi else maxi
                summ += t
                if i == n - 1:
                    ans += summ - maxi
            else:
                ans += summ - maxi
                summ = maxi = t
                color = c
        return ans
