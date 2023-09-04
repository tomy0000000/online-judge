# Let n be the length of temperatures.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        s = []
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while s and s[-1]["t"] <= t:
                s.pop()
            ans.append(s[-1]["i"] - i if s else 0)
            s.append({"t": t, "i": i})
        return ans[::-1]
