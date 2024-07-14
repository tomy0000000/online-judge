# Let n be the length of formula
#
# Time: O(n)
# Space: O(n)

import string
from collections import Counter
from typing import Optional


class Solution:
    def process_complete(self, stack: list[Counter], num: Optional[int] = 1) -> bool:
        ct = stack.pop()
        for _ in range(num):
            stack[-1] += ct
        return False

    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        length = len(formula)
        complete = False
        prev_elem = ""
        for i, c in enumerate(formula):
            if c in string.ascii_uppercase:
                if complete:
                    complete = self.process_complete(stack)
                stack[-1][c] += 1
                prev_elem = c
            if c in string.ascii_lowercase:
                if complete:
                    complete = self.process_complete(stack)
                elem = f"{prev_elem}{c}"
                stack[-1][prev_elem] -= 1
                stack[-1][elem] += 1
                prev_elem = elem
            if c == "(":
                if complete:
                    complete = self.process_complete(stack)
                stack.append(Counter())
            if c == ")":
                complete = True
            if c in string.digits:
                if i < length - 1 and formula[i + 1] in string.digits:
                    continue
                ds = i
                while formula[ds - 1] in string.digits:
                    ds -= 1
                num = int(formula[ds : i + 1])
                if complete:
                    complete = self.process_complete(stack, num)
                else:
                    stack[-1][prev_elem] += num - 1

        if complete:
            complete = self.process_complete(stack)

        c = stack.pop()
        ans = ""
        for elem in sorted(c):
            num = c[elem]
            if num == 0:
                continue
            ans += elem
            if num > 1:
                ans += str(num)
        return ans
