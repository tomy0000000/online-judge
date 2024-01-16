from random import choice


class RandomizedSet:
    # Space: O(n)
    def __init__(self):
        # Time: O(1)
        self._list = []
        self._set = set()
        self.removed = set()

    def insert(self, val: int) -> bool:
        # Time: O(1)
        not_existed = val not in self._set
        if not_existed:
            self._list.append(val)
            self._set.add(val)
        self.removed.discard(val)
        return not_existed

    def remove(self, val: int) -> bool:
        # Time: O(1)
        existed = val in self._set
        if existed:
            self._set.remove(val)
            self.removed.add(val)
        while self._list and self._list[-1] in self.removed:
            self.removed.remove(self._list.pop())
        return existed

    def getRandom(self) -> int:
        # Time: O(1) AMORTIZED
        n = choice(self._list)
        while n in self.removed:
            n = choice(self._list)
        return n
