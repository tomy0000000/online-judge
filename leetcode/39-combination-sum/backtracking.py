# Let n be the length of candidates, m be the target value
#
# Time: O(2 ^ n)
# Space: O(n ^ 2)


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if target == 0:
            return [[]]
        elif target < 0:
            return []

        candidates.sort()

        res = set()
        for i, n in enumerate(candidates):
            for comb in self.combinationSum(candidates[i:], target - n):
                res.add(tuple(comb + [n]))

        return [list(tup) for tup in res]
