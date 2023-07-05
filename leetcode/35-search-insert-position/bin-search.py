# Let n be the length of nums.
#
# Time: O(log n)
# Space: O(1)


class Solution:
    def binary_search(self, nums: list[int], target: int, begin: int, end: int):
        print(f"from {begin} to {end}")

        if end - begin < 3:
            for i in range(begin, end + 1):
                if target <= nums[i]:
                    return i

                if i != len(nums) - 1 and target < nums[i + 1]:
                    print(nums[i + 1], target)
                    return i + 1
            print("reach end")
            return end + 1

        mid_index = (end + begin) // 2
        mid = nums[mid_index]

        if mid < target:
            print("right")
            return self.binary_search(nums, target, mid_index, end)
        else:
            print("left")
            return self.binary_search(nums, target, begin, mid_index)

    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
