# Let n be the length of skill
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        counter = Counter(skill)
        total = sum(skill)
        team_num = len(skill) // 2

        if total % team_num != 0:
            return -1

        each = total // team_num
        chemistry = 0
        for n, count in counter.items():
            matching = each - n
            if matching not in counter:
                return -1
            if count != counter[matching]:
                return -1

            chemistry += n * matching * count

        return chemistry // 2
