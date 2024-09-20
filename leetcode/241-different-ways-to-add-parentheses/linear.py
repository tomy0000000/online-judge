# Let n be the length of expression
#
# Time: O(n * 2^n)
# Space: O(n * 2^n)


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if all(op not in expression for op in "+-*"):
            return [int(expression)]

        res = []
        for i, op in enumerate(expression):
            if op not in "+-*":
                continue
            left_expr = expression[0:i]
            right_expr = expression[i + 1 :]
            left = self.diffWaysToCompute(left_expr)
            right = self.diffWaysToCompute(right_expr)
            for val_l in left:
                for val_r in right:
                    if op == "+":
                        res.append(val_l + val_r)
                    if op == "-":
                        res.append(val_l - val_r)
                    if op == "*":
                        res.append(val_l * val_r)

        return res
