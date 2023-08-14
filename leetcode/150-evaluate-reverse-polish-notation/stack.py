# Let n be the length of tokens
#
# Time: O(n)
# Space: O(1)


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for op in tokens:
            if op == "+":
                stack.append(stack.pop() + stack.pop())
            elif op == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif op == "*":
                stack.append(stack.pop() * stack.pop())
            elif op == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(op))

        return stack[0]
