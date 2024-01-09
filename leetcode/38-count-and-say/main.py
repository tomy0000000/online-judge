# Time: O(n)
# Space: O(1)

from functools import cache


class Solution:
    @cache
    def _count_and_say(self, sequence: str) -> str:
        count, prev_d = 0, ""
        new_seq = ""
        for d in sequence:
            if d == prev_d:
                count += 1
            else:
                if count > 0:
                    new_seq += f"{count}{prev_d}"
                count, prev_d = 1, d
        new_seq += f"{count}{prev_d}"
        return new_seq

    @cache
    def countAndSay(self, n: int) -> str:
        current = "1"
        for i in range(n - 1):
            current = self._count_and_say(current)
        return current
