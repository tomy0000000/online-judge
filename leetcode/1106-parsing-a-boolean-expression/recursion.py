# Let n be the length of expression
#
# Time: O(n)
# Space: O(n)


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == "t":
            return True

        if expression == "f":
            return False

        if expression.startswith("!"):
            return not self.parseBoolExpr(expression[2:-1])

        quotes = 0
        subs = [""]
        for c in expression[2:-1]:
            if c == "," and quotes == 0:
                subs.append("")
                continue
            if c == "(":
                quotes += 1
            if c == ")":
                quotes -= 1
            subs[-1] += c

        if expression.startswith("&"):
            return all(self.parseBoolExpr(sub) for sub in subs)

        if expression.startswith("|"):
            return any(self.parseBoolExpr(sub) for sub in subs)
