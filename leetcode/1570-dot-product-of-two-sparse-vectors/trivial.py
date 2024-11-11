# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class SparseVector:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def dotProduct(self, vec: "SparseVector") -> int:
        return sum(a * b for a, b in zip(self.nums, vec.nums))
