# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)

from collections import Counter
from math import inf


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        c = Counter(nums)
        numbers = sorted(c)
        ans = 0
        for i, number in enumerate(numbers):
            count = c.pop(number)
            if count == 1:
                continue
            next_number = numbers[i + 1] if i + 1 < len(numbers) else inf
            gap = next_number - number - 1
            count -= 1
            if count <= gap:
                filling = count
            else:
                filling = gap
                c[next_number] += count - gap
                ans += (count - gap) * (gap + 1)
            ans += (1 + filling) * filling // 2
        return ans
