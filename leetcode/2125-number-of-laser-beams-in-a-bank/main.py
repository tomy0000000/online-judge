# Let n be the length of bank
#
# Time: O(n)
# Space: O(1)


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = 0
        beam = 0
        for row in bank:
            device = row.count("1")
            if not device:
                continue
            if not prev:
                prev = device
            else:
                beam += prev * device
                prev = device
        return beam
