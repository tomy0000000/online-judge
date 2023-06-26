# Let n be the length of nums, and m be the number of unique numbers in nums.
#
# Time: O(n + m log m)
# Space: O(m)

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)

        # Sort the table frequency, accompanied by the original num
        sorted_freq = sorted(
            [(freq, num) for num, freq in counter.items()],
            key=lambda x: x[0],
            reverse=True,
        )

        # Get the top k frequent numbers
        top_k = [num for freq, num in sorted_freq[:k]]
        return top_k
