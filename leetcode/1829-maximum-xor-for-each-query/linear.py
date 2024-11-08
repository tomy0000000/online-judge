# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        ans = []
        curr = 0
        for n in nums:
            curr ^= n
            bit = f"{bin(curr)[2:]:0>{maximumBit}}"
            inverted = "".join(str(int(b == "0")) for b in bit)
            ans.append(int(inverted, base=2))
        ans.reverse()
        return ans
