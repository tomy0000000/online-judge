# Let n be the length of s, and m be the length of t.
#
# Time: O(n + m)
# Space: O(n + m)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}
        for cs, ct in zip(s, t):
            if cs in counter:
                counter[cs] += 1
            else:
                counter[cs] = 1

            if ct in counter:
                counter[ct] -= 1
            else:
                counter[ct] = -1

        return all([count == 0 for count in counter.values()])
