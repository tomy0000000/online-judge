# Let n be the length of s1 and m be the length of s2
#
# Time: O(m)
# Space: O(n)
from collections import Counter


class Solution:
    def counter_sub_1(self, counter: dict[int, int], element: int) -> None:
        if counter[element] == 1:
            counter.pop(element)
        else:
            counter[element] -= 1

    def counter_add_1(self, counter: dict[int, int], element: int) -> None:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2

        cnt = Counter(s1)
        left = 0
        while s2[left] not in cnt and left < len(s2) - 1:
            left += 1
        if s2[left] in cnt:
            self.counter_sub_1(cnt, s2[left])

        for right in range(left + 1, len(s2)):
            if s2[right] in cnt:
                self.counter_sub_1(cnt, s2[right])
                if not cnt:
                    return True
            else:
                while s2[left] != s2[right]:
                    self.counter_add_1(cnt, s2[left])
                    left += 1
                left += 1
        return False
