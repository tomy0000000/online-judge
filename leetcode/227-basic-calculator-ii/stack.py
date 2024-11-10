# Let n be the length of s
#
# Time: O(n)
# Space: O(n)


class Solution:
    def calculate(self, s: str) -> int:
        n_str = ""
        op = "+"
        stack = []
        for c in s:
            if c.isdigit():
                n_str += c
            if c in "+-*/":
                if op == "*":
                    stack.append(stack.pop() * int(n_str))
                if op == "/":
                    stack.append(int(stack.pop() / int(n_str)))
                if op == "-":
                    stack.append(-int(n_str))
                if op == "+":
                    stack.append(int(n_str))
                n_str = ""
                op = c

        if op == "*":
            stack.append(stack.pop() * int(n_str))
        if op == "/":
            stack.append(int(stack.pop() / int(n_str)))
        if op == "-":
            stack.append(-int(n_str))
        if op == "+":
            stack.append(int(n_str))

        return sum(stack)
