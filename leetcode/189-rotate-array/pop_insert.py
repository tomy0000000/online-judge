# Let n be the length of the input list
#
# Time: O(k * n)
# Space: O(1)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())
