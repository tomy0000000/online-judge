# Let n be the length of arr
#
# Time: O(n * log(n))
# Space: O(n)


from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        c = list(Counter(arr).values())
        c.sort(reverse=True)
        while k:
            count = c.pop()
            if count > k:
                return len(c) + 1
            k -= count
        return len(c)
