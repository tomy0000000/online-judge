# Let m be the length of meetings
#
# Time: O(M log M)
# Space: O(N + M)


from collections import defaultdict


class Solution:
    def find_root(self, batches: dict[int, int], n: int) -> int:
        if batches[n] is None:
            return n
        root = self.find_root(batches, batches[n])
        batches[n] = root
        return root

    def merge_meetings(self, meetings: set[tuple[int, int]]) -> list[set[int]]:
        batches = {}
        for x, y in meetings:
            if x in batches and y in batches:
                root_x = self.find_root(batches, x)
                root_y = self.find_root(batches, y)
                if root_x != root_y:
                    batches[root_y] = x
                continue
            if x in batches:
                root = self.find_root(batches, x)
                batches[y] = root
                continue
            if y in batches:
                root = self.find_root(batches, y)
                batches[x] = root
                continue
            batches[x] = None
            batches[y] = x

        new_batches = defaultdict(set)
        for m in batches:
            root = self.find_root(batches, m)
            new_batches[root].add(m)
        return list(new_batches.values())

    def findAllPeople(
        self, n: int, meetings: list[list[int]], firstPerson: int
    ) -> list[int]:
        g_meetings = defaultdict(set)
        for x, y, t in meetings:
            g_meetings[t].add((x, y))

        for t in g_meetings:
            g_meetings[t] = self.merge_meetings(g_meetings[t])

        known = set([0, firstPerson])
        for t in sorted(g_meetings.keys()):
            for members in g_meetings[t]:
                if any([m in known for m in members]):
                    known.update(members)

        return known
