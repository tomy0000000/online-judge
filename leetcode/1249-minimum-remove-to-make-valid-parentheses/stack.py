# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        parentheses = []
        for c in s:
            if c == "(":
                parentheses.append(len(stack))
                stack.append(c)
            elif c == ")":
                if parentheses:
                    parentheses.pop()
                    stack.append(c)
            else:
                stack.append(c)
        while parentheses:
            stack.pop(parentheses.pop())
        return "".join(stack)
