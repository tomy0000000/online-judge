# Let n be the length of candidates, m be the target value
#
# Time: O(2 ^ n)
# Space: O(n ^ 2)


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if target == 0:
            return [tuple()]
        elif target < 0:
            return []

        candidates.sort()

        res = set()
        for i, n in enumerate(candidates):
            if i != 0 and n == candidates[i - 1]:
                continue
            for comb in self.combinationSum2(candidates[i + 1 :], target - n):
                res.add(comb + (n,))

        return res
