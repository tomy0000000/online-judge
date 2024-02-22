# Time: O(n)
# Space: O(n)


from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trusted_by = defaultdict(set)
        candidates = set(range(1, n + 1))
        for a, b in trust:
            candidates.discard(a)
            trusted_by[b].add(a)

        for candidate in candidates:
            if len(trusted_by[candidate]) == n - 1:
                return candidate

        return -1
