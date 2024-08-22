# Let n be the number of bits in the input number.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def findComplement(self, num: int) -> int:
        binaries = list("{0:b}".format(num))
        complements = map(lambda x: "0" if x == "1" else "1", binaries)
        return int("".join(complements), 2)
