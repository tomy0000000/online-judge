# Let n be the length of s.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "[":
                stack.append(int(stack.pop()))
            elif c == "]":
                decoded = stack.pop() * stack.pop()
                if stack and isinstance(stack[-1], str):
                    stack[-1] += decoded
                else:
                    stack.append(decoded)
            elif c.isdigit():
                if stack and isinstance(stack[-1], str) and stack[-1].isdigit():
                    stack[-1] += c
                else:
                    stack.append(c)
            else:
                if stack and isinstance(stack[-1], str):
                    stack[-1] += c
                else:
                    stack.append(c)

        return stack[0]
