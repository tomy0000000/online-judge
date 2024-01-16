from random import choice


class RandomizedSet:
    # Space: O(n)
    def __init__(self):
        # Time: O(1)
        self._locs = {}
        self._list = []

    def insert(self, val: int) -> bool:
        # Time: O(1)
        if val in self._locs:
            return False

        self._list.append(val)
        self._locs[val] = len(self._list) - 1
        return True

    def remove(self, val: int) -> bool:
        # Time: O(1)
        if val not in self._locs:
            return False

        ind = self._locs[val]

        self._locs[self._list[-1]] = ind
        self._list[ind] = self._list[-1]
        self._locs.pop(val)
        self._list.pop()
        return True

    def getRandom(self) -> int:
        # Time: O(1)
        return choice(self._list)
