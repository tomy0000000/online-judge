# Let n be the length of bombs
#
# Time: O(n ^ 2)
# Space: O(n ^ 2)


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist <= r1**2:
                    graph[i].append(j)
                if dist <= r2**2:
                    graph[j].append(i)

        maxi = 0
        for i in range(n):
            s = [i]
            visited = set()
            while s:
                b = s.pop()
                visited.add(b)
                for bb in graph[b]:
                    if bb not in visited and bb not in s:
                        s.append(bb)
            maxi = max(maxi, len(visited))
            if maxi == n:
                return n

        return maxi
