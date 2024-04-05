# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

import string


class Solution:
    def __init__(self) -> None:
        self.denyset = set()
        for l, u in zip(string.ascii_lowercase, string.ascii_uppercase):
            self.denyset.add(f"{l}{u}")
            self.denyset.add(f"{u}{l}")

    def makeGood(self, s: str) -> str:
        while True:
            prev = s
            for bad in self.denyset:
                s = s.replace(bad, "")
            if s == prev:
                break

        return s
