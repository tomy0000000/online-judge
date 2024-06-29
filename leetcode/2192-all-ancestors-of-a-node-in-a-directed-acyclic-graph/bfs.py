# Let n be the length of edges
#
# Time: O(n log n)
# Space: O(n)

from bisect import bisect_left, insort
from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        answer = [[] for _ in range(n)]
        parents = defaultdict(set)
        childs = defaultdict(set)
        roots = set(range(n))
        for begin, end in edges:
            parents[end].add(begin)
            childs[begin].add(end)
            insort(answer[end], begin)
            roots.discard(end)
        queue = deque(roots)
        while queue:
            node = queue.popleft()
            for child in childs[node]:
                parents[child].discard(node)
                for ancestor in answer[node]:
                    ind = bisect_left(answer[child], ancestor)
                    if ind >= len(answer[child]) or answer[child][ind] != ancestor:
                        answer[child].insert(ind, ancestor)
                if not parents[child]:
                    queue.append(child)
        return answer
