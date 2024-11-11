class SparseVector:
    def __init__(self, nums: list[int]):
        self.nums = []
        for i, n in enumerate(nums):
            if n == 0:
                continue
            self.nums.append((i, n))

    def dotProduct(self, vec: "SparseVector") -> int:
        ptr_1, ptr_2 = 0, 0
        result = 0
        while ptr_1 < len(self.nums) and ptr_2 < len(vec.nums):
            left = self.nums[ptr_1]
            right = vec.nums[ptr_2]

            if left[0] == right[0]:
                result += left[1] * right[1]
                ptr_1 += 1
                ptr_2 += 1
                continue

            if left[0] < right[0]:
                ptr_1 += 1
            else:
                ptr_2 += 1

        return result
