# Let n be the length of the string s.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        flag = True
        for i, b in enumerate(s):
            ans += int(int(flag) == int(b))
            flag = not flag

        return min(ans, len(s) - ans)
