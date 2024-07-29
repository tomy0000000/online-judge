# Let n be the length of rating
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        ans = 0
        for i, n in enumerate(rating):
            left_low = 0
            left_hi = 0
            right_low = 0
            right_hi = 0
            for j, nn in enumerate(rating):
                if i == j or n == nn:
                    continue
                if n < nn:
                    if i < j:
                        right_hi += 1
                    else:
                        left_hi += 1
                else:
                    if i < j:
                        right_low += 1
                    else:
                        left_low += 1
            ans += left_low * right_hi + left_hi * right_low
        return ans
