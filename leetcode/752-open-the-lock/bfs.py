# Time: O(1)
# Space: O(1)

from collections import deque


class Solution:
    def neighbors(self, comb: str) -> set[str]:
        combs = set()
        comb_list = list(comb)
        for i in range(4):
            lower, upper = comb_list.copy(), comb_list.copy()
            lower[i] = str((int(lower[i]) - 1) % 10)
            upper[i] = str((int(upper[i]) + 1) % 10)
            combs.add("".join(lower))
            combs.add("".join(upper))
        return combs

    def openLock(self, deadends: list[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = set(deadends)
        visited.add("0000")
        while queue:
            here, step = queue.popleft()
            for neighbor in self.neighbors(here):
                if neighbor == target:
                    return step + 1

                if neighbor in visited:
                    continue

                queue.append((neighbor, step + 1))
                visited.add(neighbor)

        return -1
