# Let n be the length of nums
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        converted = [
            (int("".join(str(mapping[int(d)]) for d in list(str(n)))), i, n)
            for i, n in enumerate(nums)
        ]
        return [t[2] for t in sorted(converted)]
