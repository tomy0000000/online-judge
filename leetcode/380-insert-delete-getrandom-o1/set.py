from random import choice


class RandomizedSet:
    # Space: O(n)
    def __init__(self):
        # Time: O(1)
        self._set = set()

    def insert(self, val: int) -> bool:
        # Time: O(1)
        not_existed = val not in self._set
        self._set.add(val)
        return not_existed

    def remove(self, val: int) -> bool:
        # Time: O(1)
        existed = val in self._set
        if existed:
            self._set.remove(val)
        return existed

    def getRandom(self) -> int:
        # Time: O(n)
        return choice([n for n in self._set])
