# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)

from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        counter = Counter(nums)
        matrix = []
        while counter:
            remove = []
            new_row = []
            for n, c in counter.items():
                new_row.append(n)
                if c == 1:
                    remove.append(n)
                else:
                    counter[n] -= 1

            matrix.append(new_row)

            for rm in remove:
                counter.pop(rm)

        return matrix
