# Let n be the length of arr
#
# Time: O(n)
# Space: O(n)


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        odd = set()
        even = set()
        for i, n in enumerate(arr):
            if n == 0 and n in even:
                print("two 0")
                return True
            elif n % 2 == 0:
                even.add(n)
            else:
                odd.add(n)

        even.discard(0)
        for n in odd.union(even):
            if n * 2 in even:
                return True

        return False
