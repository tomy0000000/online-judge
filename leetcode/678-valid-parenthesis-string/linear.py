# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def checkValidString(self, s: str) -> bool:
        mini, maxi = 0, 0
        for c in s:
            if c == "(":
                mini += 1
                maxi += 1
            elif c == ")":
                mini -= 1
                maxi -= 1
            else:
                mini -= 1
                maxi += 1

            if maxi < 0:
                return False
            if mini < 0:
                mini = 0

        return mini == 0
