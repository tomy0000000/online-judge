# Let n be the length of start and target
#
# Time: O(n)
# Space: O(1)

from collections import defaultdict


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        wallet = defaultdict(int)
        for i in range(len(start)):
            c1, c2 = start[i], target[i]

            if c1 == "_":
                if c2 == "L":
                    wallet["L"] -= 1
                    if wallet["R"] > 0:
                        return False

                if c2 == "R":
                    if wallet["R"] == 0:
                        return False
                    wallet["R"] -= 1

            if c1 == "L":
                if wallet["R"] > 0:
                    return False

                if c2 != "L":
                    wallet["L"] += 1

                if wallet["L"] > 0:
                    return False

                if c2 == "R":
                    if wallet["R"] == 0:
                        return False
                    wallet["R"] -= 1

            if c1 == "R":
                if wallet["L"] < 0:
                    return False

                if c2 != "R":
                    wallet["R"] += 1

                if c2 == "L":
                    wallet["L"] -= 1

        return wallet["L"] == 0 and wallet["R"] == 0
