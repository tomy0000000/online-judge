# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)

        while stack:
            if not stars:
                return False
            if stars[-1] < stack[-1]:
                return False

            stack.pop()
            stars.pop()

        return True
