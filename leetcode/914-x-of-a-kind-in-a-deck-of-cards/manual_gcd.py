# Let n be the length of deck, m be the number of unique cards
#
# Time: O(n + m log n)
# Space: O(m)


class Solution:
    def increment(self, db: list[int], val: int) -> None:
        while len(db) - 1 < val:
            db.append(0)
        db[val] += 1

    def gcd(self, x: int, y: int) -> int:
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)

    def gcds(self, arg: list[int]) -> int:
        if len(arg) == 0:
            return 0
        ret = arg[0]
        for i in range(1, len(arg)):
            ret = self.gcd(ret, arg[i])
        return ret

    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        db = [0]
        for each in deck:
            self.increment(db, each)
        return self.gcds(db) != 1
