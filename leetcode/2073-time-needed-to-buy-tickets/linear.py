# Let n be the length of nums
#
# Time: O(n)
# Space: O(1)


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        people = len(tickets)
        target = tickets[k]
        ans = target * people
        for i, t in enumerate(tickets):
            ans -= max(target - t, 0)
            if i > k and t >= target:
                ans -= 1
        return ans
