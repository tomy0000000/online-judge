class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while True:
            if nums[start] == target or nums[end] == target:
                return True
            start += 1
            end -= 1
            if end < start:
                return False