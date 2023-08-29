# Time: O(4^n / n^(3/2)) -> nth Catalan number
# Space: O(1)


class Solution:
    def generate_one(self, current: list[str], push: int, pop: int):
        if push == 0 and pop == 0:
            self.ans.append("".join(current))
            return

        if push:
            new_push = current.copy()
            new_push.append("(")
            self.generate_one(new_push, push - 1, pop)

        if pop > push:
            new_pop = current.copy()
            new_pop.append(")")
            self.generate_one(new_pop, push, pop - 1)

    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.generate_one([], n, n)
        return self.ans
