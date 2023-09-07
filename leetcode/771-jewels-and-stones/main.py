# Let n be the length of the jewels string and m be the length of the stones string.
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for each in jewels:
            ans += stones.count(each)
        return ans
