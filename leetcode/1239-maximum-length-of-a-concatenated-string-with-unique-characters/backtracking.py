# Let n be the length of arr
#
# Time: O(n * 2^n)
# Space: O(n * 2^n)

from typing import Optional


class Solution:
    def maxLength(self, arr: list[str], exists: Optional[list[str]] = None) -> int:
        if not arr:
            return 0 if not exists else len(max(exists, key=len))

        n = arr.pop()
        if len(set(n)) != len(n):
            return self.maxLength(arr, exists)

        exists = [""] if not exists else exists
        exists.extend([sub + n for sub in exists if not (set(sub) & set(n))])

        return self.maxLength(arr, exists)
