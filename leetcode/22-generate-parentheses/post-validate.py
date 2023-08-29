# Time: O(n * 2 ^ n)
# Space: O(1)


class Solution:
    def is_valid(self, current: list[str]):
        stack = []
        for p in current:
            if p == "(":
                stack.append(1)
            elif p == ")":
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False
        return True

    def generate_one(self, current: list[str], push: int, pop: int):
        if push == 0 and pop == 0:
            if self.is_valid(current):
                self.ans.append("".join(current))
            return

        if push:
            new_push = current.copy()
            new_push.append("(")
            self.generate_one(new_push, push - 1, pop)

        if pop:
            new_pop = current.copy()
            new_pop.append(")")
            self.generate_one(new_pop, push, pop - 1)

    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.generate_one([], n, n)
        return self.ans
