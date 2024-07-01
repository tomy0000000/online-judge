# Let n be the length of arr
#
# Time: O(n)
# Space: O(1)


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        acc = 0
        for n in arr:
            if n % 2 == 0:
                acc = 0
            else:
                acc += 1
            if acc == 3:
                return True
        return False
