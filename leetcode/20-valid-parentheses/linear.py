# Let n be the length of s.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        # () -> 0
        # {} -> 1
        # [] -> 2

        stack = []
        for p in s:
            if p == "(":
                stack.append(0)
            if p == "{":
                stack.append(1)
            if p == "[":
                stack.append(2)

            if p == ")":
                if not stack or stack.pop() != 0:
                    return False
            if p == "}":
                if not stack or stack.pop() != 1:
                    return False
            if p == "]":
                if not stack or stack.pop() != 2:
                    return False

        return len(stack) == 0
