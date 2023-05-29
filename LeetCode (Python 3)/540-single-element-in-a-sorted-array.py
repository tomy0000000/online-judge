class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mid = (len(nums) + 1) // 2 - 1
        if len(nums) == 1:
            return nums[0]
        if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        if mid % 2 == 0:
            if nums[mid-1] == nums[mid]:
                return self.singleNonDuplicate(nums[:mid-1])
            else:
                return self.singleNonDuplicate(nums[mid:])
        else:
            if nums[mid-1] == nums[mid]:
                return self.singleNonDuplicate(nums[mid+1:])
            else:
                return self.singleNonDuplicate(nums[:mid])
