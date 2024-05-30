# Let n be the length of arr
#
# Time: O(n ^ 2)
# Space: O(1)

from collections import Counter


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        length = len(arr)
        count = 0
        for j in range(1, length):
            tmp = arr[j - 1]
            left = Counter([tmp])
            for i in range(j - 2, -1, -1):
                tmp ^= arr[i]
                left[tmp] += 1

            tmp = arr[j]
            right = Counter([tmp])
            for k in range(j + 1, length):
                tmp ^= arr[k]
                right[tmp] += 1

            common = set(left.keys()) & set(right.keys())
            for key in common:
                count += left[key] * right[key]

        return count
