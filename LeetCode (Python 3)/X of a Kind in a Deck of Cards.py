def increment(db, val):
    while len(db)-1 < val:
        db.append(0)
    db[val] += 1

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def gcds(arg):
    if len(arg) == 0:
        return 0
    ret = arg[0]
    for i in range(1, len(arg)):
        ret = gcd(ret, arg[i])
    return ret

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        db = [0]
        for each in deck:
            increment(db, each)
        return gcds(db[1:]) != 1
