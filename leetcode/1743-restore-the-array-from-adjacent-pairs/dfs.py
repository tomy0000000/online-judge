# Let n be the length of adjacentPairs
#
# Time: O(n)
# Space: O(n)


class Solution:
    def add_mapping(self, mapping: dict[int, set[int]], begin: int, to: int) -> None:
        if begin in mapping:
            mapping[begin].add(to)
        else:
            mapping[begin] = {to}

    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        # Build maps
        mapping = {}
        for left, right in adjacentPairs:
            self.add_mapping(mapping, left, right)
            self.add_mapping(mapping, right, left)

        # Find head
        head = None
        for e in mapping:
            if len(mapping[e]) == 1:
                head = e
                break

        # Concat
        ans = [head]
        cur = head
        prev = head
        while True:
            dirs = mapping[cur]
            dirs.discard(prev)
            if not dirs:
                break
            following = dirs.pop()
            ans.append(following)
            prev, cur = cur, following

        return ans
