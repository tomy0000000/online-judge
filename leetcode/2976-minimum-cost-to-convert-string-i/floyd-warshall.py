# Let n be the length of source
#
# Time: O(n)
# Space: O(n)

import string
from math import inf


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        cost_map = {
            c: {cc: inf for cc in string.ascii_lowercase}
            for c in string.ascii_lowercase
        }

        for c in string.ascii_lowercase:
            cost_map[c][c] = 0

        for start, end, c in zip(original, changed, cost):
            cost_map[start][end] = min(cost_map[start][end], c)

        for k in string.ascii_lowercase:
            for i in string.ascii_lowercase:
                for j in string.ascii_lowercase:
                    cost_map[i][j] = min(
                        cost_map[i][j], cost_map[i][k] + cost_map[k][j]
                    )

        total_cost = sum(cost_map[cs][ct] for cs, ct in zip(source, target))
        return total_cost if total_cost != inf else -1
