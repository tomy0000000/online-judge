# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        if s[0] == ")" and locked[0] == "1":
            return False

        unlocked = []
        locked_open = []
        for i, (c, l) in enumerate(zip(s, locked)):
            if l == "0":
                unlocked.append(i)
            if l == "1":
                if c == "(":
                    locked_open.append(i)
                if c == ")":
                    if locked_open:
                        locked_open.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False

        while locked_open and unlocked:
            if locked_open[-1] < unlocked[-1]:
                locked_open.pop()
                unlocked.pop()
            else:
                return False

        return not locked_open
