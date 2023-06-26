# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Special case, if there are more than two 0
        # The results will be all zero
        if nums.count(0) >= 2:
            return [0] * len(nums)

        # In cases where many elements are duplicate, we should only compute once
        # Initialize the hash map here
        # and use the same loop for counting
        unique_products = {}
        counter: dict = {}
        for n in nums:
            unique_products[n] = 1
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        # Mutiplication
        already_multiplied = set()
        for index, n in enumerate(nums):
            for num in unique_products:
                # If the number presents twice, one of them should be multiplied
                if num != n or (n in already_multiplied):
                    unique_products[num] *= n
                else:
                    already_multiplied.add(n)

        # Compose the array from hash map
        return [unique_products[n] for n in nums]
